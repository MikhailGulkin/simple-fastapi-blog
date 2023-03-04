from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column, relationship
)

from src.infrastructure.db.models.base import BaseAlchemyModels


class User(BaseAlchemyModels):
    __tablename__ = 'user_table'

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

    posts: Mapped[list["Post"]] = relationship(back_populates="user")
