from fastapi import APIRouter
from .upload import router as upload
from .image_add import router as add_image

router = APIRouter()

router.include_router(upload)
router.include_router(add_image)