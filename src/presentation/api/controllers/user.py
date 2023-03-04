from fastapi import (
    APIRouter,
    Response,
    status
)
from fastapi.params import Depends

from src.domain.blog.dto import (
    CreateUserDTO,
    UserDTO,
    UpdateUserDTO
)
from src.domain.blog.exceptions import UserNotExists
from src.domain.blog.usecases import UserServices

from src.presentation.api.controllers.requests.user import (
    CreateUserRequest,
    UpdateUserRequest
)
from src.presentation.api.controllers.responses import UserDeleteResponse
from src.presentation.api.controllers.responses.exceptions import \
    NotFoundUserError
from src.presentation.api.di.providers.services import (
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


@router.delete('/delete-post/{user_id}')
async def delete_post(
        user_id: int,
        response: Response,
        user_services: UserServices = Depends(get_user_services)
) -> UserDeleteResponse | NotFoundUserError:
    try:
        await user_services.delete_user(user_id)
        return UserDeleteResponse()
    except UserNotExists:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NotFoundUserError()
