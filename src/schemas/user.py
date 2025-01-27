import bcrypt
from pydantic import BaseModel, field_validator


class UserData(BaseModel):
    username: str
    password: str
    role: str

    # @field_validator("password")
    # def hash_password(cls, value):
    #     salt = bcrypt.gensalt()
    #     hashed_password = bcrypt.hashpw(value.encode('utf-8'), salt)
    #     return hashed_password.decode('utf-8')


class UserCreateRequest(UserData):
    class Config:
        form_attributes = True


class UserCreateResponse(UserData):
    id: int

    class Config:
        from_attributes = True
