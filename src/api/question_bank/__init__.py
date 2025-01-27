from fastapi import APIRouter
from .upload import router as upload
from .image_add import router as add_image
from .random_choose import router as random_choose

router = APIRouter()

router.include_router(upload)
router.include_router(add_image)
router.include_router(random_choose)