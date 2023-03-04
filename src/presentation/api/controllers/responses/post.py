from pydantic import BaseModel, Field


class PostDeleteResponse(BaseModel):
    message: str = Field("The post has been deleted", const=True)
