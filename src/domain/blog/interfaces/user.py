from src.domain.common.usecases.base import BaseUseCase
from src.dal.db.uow import UnitOfWork


class UserUseCase(BaseUseCase):
    def __init__(self, uow: UnitOfWork) -> None:
        super().__init__(uow)

