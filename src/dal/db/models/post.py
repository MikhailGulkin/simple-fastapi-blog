from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    ForeignKey, TIMESTAMP
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.dal.db.models.base import BaseAlchemyModels


class Post(BaseAlchemyModels):
    __tablename__ = 'Post'

    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    author_id: Mapped[int] = mapped_column(
        ForeignKey('User.id'),
        nullable=False
    )
    title: Mapped[str] = mapped_column(
        String(125),
        nullable=False,
    )
    summary: Mapped[str] = mapped_column(
        String(240),
        nullable=False
    )
    body: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    published_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=datetime.now()
    )