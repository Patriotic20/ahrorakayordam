from fastapi import APIRouter
from .question_bank import router as question_bank

router = APIRouter()

router.include_router(question_bank)