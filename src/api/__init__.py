from fastapi import APIRouter
from .question_bank import router as question_bank
from .user_authen import router as user_router

router = APIRouter()


router.include_router(question_bank)
router.include_router(user_router)
