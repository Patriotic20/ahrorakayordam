from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src.crud.department_crud import get_department, get_departments, create_department, update_department, delete_department
from src.schemas.department_schema import DepartmentCreate, DepartmentUpdate

router = APIRouter()

@router.get("/departments/{department_id}")
def read_department(department_id: int, db: Session = Depends(get_db)):
    return get_department(db, department_id)

@router.get("/departments/")
def read_departments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_departments(db, skip, limit)

@router.post("/departments/")
def create_new_department(department: DepartmentCreate, db: Session = Depends(get_db)):
    return create_department(db, department)

@router.put("/departments/{department_id}")
def modify_department(department_id: int, department: DepartmentUpdate, db: Session = Depends(get_db)):
    return update_department(db, department_id, department)

@router.delete("/departments/{department_id}")
def remove_department(department_id: int, db: Session = Depends(get_db)):
    return delete_department(db, department_id)
