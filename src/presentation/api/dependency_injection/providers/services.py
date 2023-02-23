from fastapi import Depends

from src.business.user.usecases import UserServices
from src.dal.db.uow import UnitOfWork
from src.presentation.api.dependency_injection.providers.db import uow_provider


def get_user_services(uow: UnitOfWork = Depends(uow_provider)) -> UserServices:
    return UserServices(uow)
