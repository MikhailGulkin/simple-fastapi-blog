from fastapi import APIRouter
from src.presentation.api.controllers.user import router as user_router


def setup_controllers(router: APIRouter) -> None:
    router.include_router(user_router)
