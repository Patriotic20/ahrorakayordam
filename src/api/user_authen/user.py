from datetime import timedelta, datetime

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.base.db import get_db
from src.exceptions import UserNotFound, CredentialsException
from src.models.user import User
from src.schemas.user import UserCreateResponse, UserCreateRequest
from src.utils import verify_password, create_access_token

users_router = APIRouter(prefix='/users', tags=["Users"])


@users_router.post('/register', response_model=UserCreateResponse)
def register_user(user_create_data: UserCreateRequest, db: Session = Depends(get_db)):
    new_user = User(**user_create_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@users_router.post("/login")
def login_user(login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = db.execute(select(User).where(login_form.username == User.username))
    user = result.scalar_one_or_none()

    if not user:
        raise UserNotFound

    if not verify_password(login_form.password, user.password):
        raise CredentialsException

    access_token = create_access_token(data={"username":user.username, "exp":datetime.utcnow() + timedelta(minutes=15)})
    return {'access_token':access_token}


@users_router.delete("/")
def delete_user():
    ...