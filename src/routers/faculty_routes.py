from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db import get_db
from src.crud.faculty_crud import get_faculty, get_faculties, create_faculty, update_faculty, delete_faculty
from src.schemas.faculty_schema import FacultyCreate, FacultyUpdate

router = APIRouter()

@router.get("/faculties/{faculty_id}")
def read_faculty(faculty_id: int, db: Session = Depends(get_db)):
    return get_faculty(db, faculty_id)

@router.get("/faculties/")
def read_faculties(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_faculties(db, skip, limit)

@router.post("/faculties/")
def create_new_faculty(faculty: FacultyCreate, db: Session = Depends(get_db)):
    return create_faculty(db, faculty)

@router.put("/faculties/{faculty_id}")
def modify_faculty(faculty_id: int, faculty: FacultyUpdate, db: Session = Depends(get_db)):
    return update_faculty(db, faculty_id, faculty)

@router.delete("/faculties/{faculty_id}")
def remove_faculty(faculty_id: int, db: Session = Depends(get_db)):
    return delete_faculty(db, faculty_id)
