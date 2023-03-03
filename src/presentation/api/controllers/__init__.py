from fastapi import APIRouter
from src.presentation.api.controllers.user import router as user_router
from src.presentation.api.controllers.post import router as post_router


def setup_controllers(router: APIRouter) -> None:
    router.include_router(user_router)
    router.include_router(post_router)
