from fastapi import APIRouter
from fastapi.params import Depends

from src.business.blog.dto import (
    CreatePostDTO,
    PostDTO,
    UpdatePostDTO

)
from src.business.blog.usecases import PostServices

from src.presentation.api.controllers.requests import (
    CreatePostRequest, UpdatePostRequest,
)
from src.presentation.api.dependency_injection.providers.services import (
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
) -> PostDTO:
    return await post_services.get_post_by_id(id_)


@router.patch('/update-post')
async def update_post(
        id_: int,
        post: UpdatePostRequest,
        post_services: PostServices = Depends(get_post_services)
) -> PostDTO:
    return await post_services.update_post(
        UpdatePostDTO(id=id_, **post.dict())
    )
