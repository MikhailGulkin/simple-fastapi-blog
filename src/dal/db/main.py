from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import DeclarativeBase


class BaseAlchemyModels(DeclarativeBase):
    pass


def create_engine(database_url: str) -> AsyncEngine:

    return create_async_engine(
        database_url,
    )


def build_sessions(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    return async_sessionmaker(
        bind=engine,
        autoflush=False,  # Фиктивные изменения
        expire_on_commit=False  # Ручные коммиты
    )

