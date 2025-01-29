from datetime import timedelta, datetime

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.future import select
from sqlalchemy.orm import Session 

from src.base.db import get_db
from src.exceptions import UserNotFound, CredentialsException, NotationRoleException
from src.models import Teacher, Student
from src.models.admins import Admin
# from src.models.user import User
from src.schemas.user import UserCreateResponse
from src.utils import verify_password, create_access_token

users_router = APIRouter(prefix='/users', tags=["Users"])

@users_router.post('/register', response_model=UserCreateResponse)
def register_user(username: str, password:str, role:str, db: Session = Depends(get_db)):
    new_user = ( Teacher(username=username,password=password,role=role),
                 Admin(username=username,password=password,role=role),
                 Student(username=username,password=password,role=role))

    if role =='admin':
        new_admin = Admin(username=username, password=password)
        db.add(new_admin)

    elif role =='teacher':
        new_teacher = Teacher(username=username, password=password)
        db.add(new_teacher)

    elif role == 'student':
        new_student= Student(username=username, password=password)
        db.add(new_student)
    else :
        raise NotationRoleException

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return


# @users_router.post('/register', response_model=UserCreateResponse)
# def register_user(user_create_data: UserCreateRequest, db: Session = Depends(get_db)):
#     new_user = User(**user_create_data.model_dump())
#
#     if user_create_data.role =='admin':
#         new_admin = Admin(**new_user.model_dump())
#         db.add(new_admin)
#
#     elif user_create_data.role =='teacher':
#         new_teacher = Admin(**new_user.model_dump())
#         db.add(new_teacher)
#
#     elif user_create_data.role == 'student':
#         new_student= Admin(**new_user.model_dump())
#         db.add(new_student)
#     else :
#         raise NotationRoleException
#
#     db.commit()
#     db.refresh(new_user)
#     return new_user




@users_router.post("/login")
def login_user(login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    result = db.execute(select(User).where(User.username == login_form.username))
    user = result.scalar_one_or_none()

    if not user:
        raise UserNotFound

    if not verify_password(login_form.password, user.password):
        raise CredentialsException

    access_token = create_access_token(data=dict(username=user.username , user_id = user.id), expires_delta = timedelta(minutes=15))

    # access_token = create_access_token(data={"username":user.username, "exp":datetime.utcnow() + timedelta(minutes=15)})
    return {'access_token':access_token}


@users_router.delete("/")
def delete_user():
    ...