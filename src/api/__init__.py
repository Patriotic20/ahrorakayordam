from fastapi import APIRouter
from .question_bank import router as question_bank
from .user_authen import router as user_router
from .routers import router as department_router

router = APIRouter()


router.include_router(question_bank)
router.include_router(user_router)
router.include_router(department_router)