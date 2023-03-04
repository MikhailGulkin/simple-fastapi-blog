from pydantic import BaseModel


class BasePost(BaseModel):
    author_id: int
    title: str
    summary: str
    body: str


class CreatePostRequest(BasePost):
    pass


class UpdatePostRequest(BasePost):
    author_id: int | None = None
    title: str | None = None
    summary: str | None = None
    body: str | None = None
