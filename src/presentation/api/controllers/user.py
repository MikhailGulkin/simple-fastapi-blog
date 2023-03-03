from fastapi import APIRouter
from fastapi.params import Depends

from src.business.blog.dto import (
    CreateUserDTO,
    UserDTO,
    UpdateUserDTO
)
from src.business.blog.usecases import UserServices

from src.presentation.api.controllers.requests.user import (
    CreateUserRequest,
    UpdateUserRequest
)
from src.presentation.api.dependency_injection.providers.services import (
    get_user_services
)

router = APIRouter(
    prefix='/user',
    tags=['user']
)


@router.get('/get-user')
async def get_user_by_id(
        id_: int,
        user_services: UserServices = Depends(get_user_services)
) -> UserDTO:
    return await user_services.get_user_by_id(id_)


@router.get('/get-all-user')
async def get_all_users(
        user_services: UserServices = Depends(get_user_services)
) -> list[UserDTO]:
    users = await user_services.get_all_users()
    return users


@router.post('/create-user')
async def create_user(
        user: CreateUserRequest,
        user_services: UserServices = Depends(get_user_services),
) -> UserDTO:
    return await user_services.create_user(CreateUserDTO(**user.dict()))


@router.patch('/update-user')
async def update_user(
        id_: int,
        user: UpdateUserRequest,
        user_services: UserServices = Depends(get_user_services)
) -> UserDTO:
    return await user_services.update_user(
        UpdateUserDTO(id=id_, **user.dict())
    )
