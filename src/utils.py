import typing
import bcrypt
from jose import jwt, JWTError
from fastapi import HTTPException, status
from datetime import timedelta , datetime

from .base.config import settings
from .exceptions import UserNotFound


def create_access_token(data: typing.Dict ,  expires_delta: timedelta = timedelta(minutes=15)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp" : expire})
    
    encoded_jwt = jwt.encode(to_encode , settings.SECRET_KEY , algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        return payload
    except JWTError:
        raise UserNotFound

def get_user_from_token(token : str):
    payload = jwt.decode(token , settings.SECRET_KEY , algorithms=settings.ALGORITHM)
    
    user_id = payload.get("user_id")
    if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User ID not found in token")
    return user_id
    
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'),
                          hashed_password.encode('utf-8')
                          )
