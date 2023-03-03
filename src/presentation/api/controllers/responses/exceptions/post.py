from pydantic import Field

from src.presentation.api.controllers.responses.exceptions.base import ApiError


class PostAlreadyExistsError(ApiError):
    detail = Field("Post already exists", const=True)