from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.domain.blog.dto import CreatePostDTO
from src.dal.db.models import Post
from src.dal.db.repositories.base import BaseRepository


class PostRepository(BaseRepository[Post]):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        super().__init__(Post, session)

    async def create_post(
            self,
            post_dto: CreatePostDTO
    ) -> Post:
        post = Post(
            author_id=post_dto.author_id,
            title=post_dto.title,
            summary=post_dto.summary,
            body=post_dto.body,
        )
        self.session.add(post)
        await self.session.flush()
        return post

    async def get_post_by_id(
            self,
            id_: int
    ) -> Post:
        return await super().get_by_id(id_)

    async def get_all_posts(self) -> list[Post]:
        return await super().get_all()

    async def update_post(
            self,
            id_: int,
            **kwargs
    ) -> None:
        await super().update_obj(id_, **kwargs)

    async def delete_post(
            self,
            id_: int
    ) -> None:
        await super().delete_obj(id_)
