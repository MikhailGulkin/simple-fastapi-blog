from sqlalchemy.ext.asyncio import AsyncSession

from dal.db.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    def create_user(self, username, ) -> User: