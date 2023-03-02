from fastapi import APIRouter
from fastapi.params import Depends

from src.business.dto import (
    CreateUserDTO,
    UserDTO,
    UpdateUserDTO
)
from src.business.user.usecases import UserServices

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


@router.post('/create-user')
async def create_user(
        user: CreateUserRequest,
        user_services: UserServices = Depends(get_user_services),
) -> UserDTO:
    return await user_services.create_user(CreateUserDTO(**user.dict()))


@router.get('/get-user')
async def get_user_by_id(
        id_: int,
        user_services: UserServices = Depends(get_user_services)
) -> UserDTO:
    return await user_services.get_user_by_id(id_)


@router.get('/get-all-user')
async def get_user_by_id(
        user_services: UserServices = Depends(get_user_services)
) -> list[UserDTO]:
    return await user_services.get_all_users()


@router.patch('/update-user')
async def update_user(
        id_: int,
        user: UpdateUserRequest,
        user_services: UserServices = Depends(get_user_services)
) -> UserDTO:
    return await user_services.update_user(
        UpdateUserDTO(id=id_, **user.dict())
    )
