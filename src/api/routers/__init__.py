from fastapi import APIRouter

from .department_routes import router as dep_router
from .faculty_routes import router as fac_router

router = APIRouter()

router.include_router(dep_router)
router.include_router(fac_router)
