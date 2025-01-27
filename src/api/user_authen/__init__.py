from fastapi import APIRouter

from .students import student_router
from .user import users_router as user

router = APIRouter()
router.include_router(user)
router.include_router(student_router)