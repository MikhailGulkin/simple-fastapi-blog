from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.dal.db.main import BaseAlchemyModels


class User(BaseAlchemyModels):
    __tablename__ = 'User'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
        unique=True
    )
    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )

    password: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
    )

