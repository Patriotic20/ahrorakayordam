from fastapi import APIRouter
from .user import users_router as user

router = APIRouter()
router.include_router(user)