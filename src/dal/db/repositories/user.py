from sqlalchemy.ext.asyncio import AsyncSession

from src.business.dto.user import CreateUserDTO
from src.dal.db.models.user import User


class UserRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create_user(
            self,
            user_dto: CreateUserDTO
    ) -> User:
        user = User(
            username=user_dto.username,
            email=user_dto.email,
            password=user_dto.password
        )
        self.session.add(user)
        return user

