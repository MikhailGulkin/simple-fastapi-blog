from fastapi import APIRouter
from fastapi.params import Depends

from src.business.dto.user import (
    CreateUserDTO,
    UserDTO
)
from src.business.user.usecases import UserServices

from src.presentation.api.controllers.requests.user import CreateUserRequest
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
