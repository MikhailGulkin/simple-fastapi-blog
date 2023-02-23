from pydantic.main import BaseModel


class CreateUserDTO(BaseModel):
    username: str
    email: str
    password: str


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True
