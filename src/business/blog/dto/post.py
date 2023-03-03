from datetime import datetime

from pydantic.main import BaseModel


class BasePostDTO(BaseModel):
    author_id: int
    title: str
    summary: str
    body: str

    class Config:
        orm_mode = True


class CreatePostDTO(BasePostDTO):
    pass


class UpdatePostDTO(BasePostDTO):
    id: int
    author_id: int | None = None
    title: str | None = None
    summary: str | None = None
    body: str | None = None


class PostDTO(BasePostDTO):
    id: int
    published_at: datetime
