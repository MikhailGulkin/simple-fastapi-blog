
from src.business.blog.dto.user import (
    CreateUserDTO,
    UserDTO,
    UpdateUserDTO
)
from src.business.common.usecases.base import BaseUseCase

from src.dal.db.uow import UnitOfWork


class UserUseCase(BaseUseCase):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)


class CreateUser(UserUseCase):
    async def __call__(self, user_dto: CreateUserDTO) -> UserDTO:
        user = await self.uow.blog_holder.user_repo.create_user(
            user_dto
        )
        await self.uow.commit()
        return user


class GetUserById(UserUseCase):
    async def __call__(self, id_: int) -> UserDTO:
        user = await self.uow.blog_holder.user_repo.get_user_by_id(
            id_
        )
        return user


class GetUsers(UserUseCase):
    async def __call__(self) -> list[UserDTO]:
        users = await self.uow.blog_holder.user_repo.get_all_users()
        return users


class UpdateUser(UserUseCase):
    async def __call__(self, user_update_dto: UpdateUserDTO) -> None:
        await self.uow.blog_holder.user_repo.update_user(
            user_update_dto.id,
            **user_update_dto.dict(
                exclude_none=True,
                exclude=set('id')
            )
        )


class UserServices:
    def __init__(self, uow: UnitOfWork) -> None:
        self.uow = uow

    async def create_user(self, user_dto: CreateUserDTO) -> UserDTO:
        return await CreateUser(self.uow)(user_dto)

    async def get_user_by_id(self, id_: int) -> UserDTO:
        return await GetUserById(self.uow)(id_)

    async def get_all_users(self) -> list[UserDTO]:
        return await GetUsers(self.uow)()

    async def update_user(
            self,
            update_user_dto: UpdateUserDTO
    ) -> UserDTO:
        await UpdateUser(self.uow)(update_user_dto)
        return await GetUserById(self.uow)(update_user_dto.id)
