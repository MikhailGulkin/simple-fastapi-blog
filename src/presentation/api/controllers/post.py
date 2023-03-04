from fastapi import (
    APIRouter,
    Response,
    status
)
from fastapi.params import Depends

from src.domain.blog.dto import (
    CreatePostDTO,
    PostDTO,
    UpdatePostDTO

)
from src.domain.blog.exceptions import PostNotExists
from src.domain.blog.usecases import PostServices

from src.presentation.api.controllers.requests import (
    CreatePostRequest,
    UpdatePostRequest,
)
from src.presentation.api.controllers.responses import PostDeleteResponse
from src.presentation.api.controllers.responses.exceptions import (
    NotFoundPostError
)
from src.presentation.api.di.providers.services import (
    get_post_services
)

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('/create-post')
async def create_user(
        post: CreatePostRequest,
        post_services: PostServices = Depends(get_post_services),
) -> PostDTO:
    post = await post_services.create_post(CreatePostDTO(**post.dict()))
    return post


@router.get('/get-all-post')
async def get_post_by_id(
        post_services: PostServices = Depends(get_post_services)
) -> list[PostDTO]:
    return await post_services.get_all_posts()


@router.get('/get-post')
async def get_post_by_id(
        id_: int,
        post_services: PostServices = Depends(get_post_services)
) -> PostDTO | NotFoundPostError:
    try:
        return await post_services.get_post_by_id(id_)
    except PostNotExists:
        return NotFoundPostError()


@router.patch('/update-post')
async def update_post(
        id_: int,
        post: UpdatePostRequest,
        post_services: PostServices = Depends(get_post_services)
) -> PostDTO:
    return await post_services.update_post(
        UpdatePostDTO(id=id_, **post.dict())
    )


@router.delete('/delete-post')
async def delete_post(
        id_: int,
        response: Response,
        post_services: PostServices = Depends(get_post_services)
) -> PostDeleteResponse | NotFoundPostError:
    try:
        await post_services.delete_post(id_)
        return PostDeleteResponse()
    except PostNotExists:
        response.status_code = status.HTTP_404_NOT_FOUND
        return NotFoundPostError()
