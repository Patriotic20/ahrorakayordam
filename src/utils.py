import typing
import bcrypt
from jose import jwt, JWTError

from .base.config import settings
from .exceptions import UserNotFound


def create_access_token(data: typing.Dict):
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise UserNotFound


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'),
                          hashed_password.encode('utf-8')
                          )
