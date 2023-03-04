from fastapi import Depends

from src.domain.blog.usecases import (
    UserServices,
    PostServices
)

from src.infrastructure.db.uow import UnitOfWork
from src.presentation.api.di.providers.db import uow_provider


def get_user_services(uow: UnitOfWork = Depends(uow_provider)) -> UserServices:
    return UserServices(uow)


def get_post_services(uow: UnitOfWork = Depends(uow_provider)) -> PostServices:
    return PostServices(uow)
