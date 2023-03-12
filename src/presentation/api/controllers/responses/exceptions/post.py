from pydantic import Field

from src.presentation.api.controllers.responses.exceptions.base import ApiError


class NotFoundPostError(ApiError):
    detail = Field("Not found post", const=True)
