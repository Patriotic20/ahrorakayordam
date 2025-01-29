from typing import Optional, Dict, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.base.db import get_db
from src.models import Student
from src.schemas.students import StudentCreateResponse


student_router = APIRouter(prefix='/students', tags=['Students'])


@student_router.post("/add", response_model=StudentCreateResponse)
def add_student(username: str, password: str, test: Optional[Dict[str, Any]] = None, db: Session = Depends(get_db)):
    
    new_student = Student(username=username, password=password, test=test)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return StudentCreateResponse.from_orm(new_student)



@student_router.post("/add_variant")
def test_response(password: str, db: Session = Depends(get_db)):
    test = db.execute(password==password)

    ...