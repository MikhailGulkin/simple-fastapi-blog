from abc import ABC

from src.business.dto.user import CreateUserDTO
from src.dal.db.uow import UnitOfWork


class UserUseCase(ABC):
    def __init__(self, uow: UnitOfWork):
        self.uow = uow


class CreateUser(UserUseCase):
    async def __call__(self, user_dto: CreateUserDTO):
        user = await self.uow.user_repo.create_user(
            user_dto
        )
        await self.uow.commit()
        return user


class UserServices:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def create_user(self, user_dto: CreateUserDTO):
        return await CreateUser(self.uow)(user_dto)
