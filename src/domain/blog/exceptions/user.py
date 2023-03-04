from src.domain.common.exceptions import AppException


class UserException(AppException):
    """Base post exception"""

    pass


class UserNotExists(UserException):
    """User not exists error"""

    pass


