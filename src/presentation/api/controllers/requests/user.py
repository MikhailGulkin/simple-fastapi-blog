from pydantic.main import BaseModel


class BaseUser(BaseModel):
    username: str
    email: str
    password: str


class CreateUserRequest(BaseUser):
    pass
