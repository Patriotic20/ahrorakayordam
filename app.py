from fastapi import FastAPI
from src.routers import faculty_routes, department_routes

app = FastAPI()

app.include_router(faculty_routes.router, prefix="/api", tags=["Faculties"])
app.include_router(department_routes.router, prefix="/api", tags=["Departments"])
