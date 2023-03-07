import pytest
import pytest_asyncio
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker

from src.infrastructure.db.models import (
    User,
    Post
)


@pytest_asyncio.fixture(scope="function")
async def create_user_in_database(db_session_test: sessionmaker):
    async def create_user_in_database_wrap(
            user_id: int,
            username: str,
            email: str,
            password: str
    ):
        async with db_session_test() as session:
            await session.execute(
                insert(User).values(
                    id=user_id,
                    username=username,
                    email=email,
                    password=password
                )
            )
            await session.commit()

    return create_user_in_database_wrap


@pytest.fixture
def user_data():
    return {
        'user_id': 1,
        "username": "string",
        "email": "string",
        "password": "string"
    }


@pytest_asyncio.fixture(scope="function")
async def create_post_in_database(db_session_test: sessionmaker):
    async def create_post_in_database_wrap(
            post_id: int,
            author_id: int,
            title: str,
            summary: str,
            body: str,
    ):
        async with db_session_test() as session:
            await session.execute(
                insert(Post).values(
                    id=post_id,
                    author_id=author_id,
                    title=title,
                    summary=summary,
                    body=body
                )
            )
            await session.commit()

    return create_post_in_database_wrap


@pytest.fixture
def post_data():
    return {
        'post_id': 1,
        "author_id": 1,
        "title": "string",
        "summary": "string",
        "body": "string"
    }
