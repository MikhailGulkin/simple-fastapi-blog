from sqlalchemy.ext.asyncio import AsyncSession

from src.dal.db.repositories.user import UserRepository


class SqlAlchemyUOW:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()


class UnitOfWork(SqlAlchemyUOW):
    def __init__(self, session: AsyncSession):
        super().__init__(session)
        self.user_repo = UserRepository(session)
