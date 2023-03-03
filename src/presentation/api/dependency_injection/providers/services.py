from fastapi import Depends

from src.business.blog.usecases import (
    UserServices,
    PostServices
)

from src.dal.db.uow import UnitOfWork
from src.presentation.api.dependency_injection.providers.db import uow_provider


def get_user_services(uow: UnitOfWork = Depends(uow_provider)) -> UserServices:
    return UserServices(uow)


def get_post_services(uow: UnitOfWork = Depends(uow_provider)) -> PostServices:
    return PostServices(uow)
