import asyncio
from collections.abc import AsyncGenerator, Generator
from typing import Any

import pytest
import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.orm import close_all_sessions, sessionmaker

from src.config import get_settings
from src.infrastructure.db.main import build_sessions, create_engine
from src.presentation.api.controllers import setup_controllers
from src.presentation.api.di import setup_di


def build_test_app() -> FastAPI:
    """Factory test application"""

    app = FastAPI()
    settings = get_settings()

    db_engine = create_engine(settings.DB_URL)

    setup_di(app, build_sessions(db_engine))

    setup_controllers(app.router)

    return app


@pytest_asyncio.fixture(scope="session")
async def db_session_test() -> sessionmaker:
    yield build_sessions(create_engine(get_settings().DB_URL))
    close_all_sessions()


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function", autouse=True)
async def clean_tables(db_session_test) -> None:
    tables = ("user_table", "post_table")
    async with db_session_test() as session:
        for table in tables:
            statement = text(f"""TRUNCATE TABLE {table} CASCADE;""")
            await session.execute(statement)
            await session.commit()


@pytest_asyncio.fixture(scope="function")
async def client() -> AsyncGenerator[AsyncClient, Any]:
    async with AsyncClient(app=build_test_app(), base_url="http://test") as client_:
        yield client_
