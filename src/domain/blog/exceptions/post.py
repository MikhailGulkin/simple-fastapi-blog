from src.domain.common.exceptions import AppException


class PostException(AppException):
    """Base post exception"""

    pass


class PostNotExists(PostException):
    """Post not exists error"""

    pass


