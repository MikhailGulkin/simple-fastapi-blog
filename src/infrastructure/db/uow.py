from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.repositories import UserRepository, PostRepository


class SqlAlchemyUOW:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class BlogHolder:
    def __init__(self, session: AsyncSession) -> None:
        self.user_repo = UserRepository(session)
        self.post_repo = PostRepository(session)


class UnitOfWork(SqlAlchemyUOW):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

        self.blog_holder = BlogHolder(session)
