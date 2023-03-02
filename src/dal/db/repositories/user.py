
from sqlalchemy.ext.asyncio import AsyncSession

from src.business.dto.user import CreateUserDTO
from src.dal.db.models.user import User
from src.dal.db.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        super().__init__(User, session)

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

    async def get_user_by_id(
            self,
            id_: int
    ) -> User:
        return await super().get_by_id(id_)

    async def get_all_users(self) -> list[User]:
        return await super().get_all()

    async def update_user(
            self,
            id_: int,
            **kwargs
    ) -> None:
        await super().update_obj(id_, **kwargs)
