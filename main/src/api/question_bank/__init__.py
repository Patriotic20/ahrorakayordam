from fastapi import APIRouter
from .upload import router as upload

router = APIRouter()

router.include_router(upload)