import typing
from functools import wraps
from sqlalchemy.orm import Session

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select

from src.base.db import get_db
from src.exceptions import CredentialsException, InvalidRoleException
from .models import Admin, Teacher, Student
# from .models.user import User

from  .utils import verify_token

security_schema = OAuth2PasswordBearer(tokenUrl='/user/login')


def get_current_user(token: str = Depends(security_schema), db: Session = Depends(get_db)):
    payload = verify_token(token)
    username: str = payload.get("username")

    if username is None:
        raise CredentialsException

    result = db.execute((select(Admin).filter(Admin.username == username)) or (select(Teacher).filter(Teacher.username==username)) or (select(Student).filter(Student.username==username)))
    user = result.scalars().first()

    if user is None:
        raise CredentialsException

    return user


def has_access(roles: typing.List[str]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = kwargs.get('current_user')

            if user.role not in roles:
                raise InvalidRoleException

            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


def get_admin_user(user: Admin = Depends(get_current_user)):
    if user.username != 'admin':
        raise CredentialsException
    return user
