from sqlalchemy.orm import Session
from src.models.models import Faculty  
from src.schemas.faculty_schema import FacultyCreate, FacultyUpdate  
def get_faculty(db: Session, faculty_id: int):
    return db.query(Faculty).filter(Faculty.id == faculty_id).first()

def get_faculties(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Faculty).offset(skip).limit(limit).all()

def create_faculty(db: Session, faculty: FacultyCreate):
    db_faculty = Faculty(name=faculty.name, description=faculty.description)
    db.add(db_faculty)
    db.commit()
    db.refresh(db_faculty)
    return db_faculty

def update_faculty(db: Session, faculty_id: int, faculty: FacultyUpdate):
    db_faculty = get_faculty(db, faculty_id)
    if db_faculty:
        for key, value in faculty.dict(exclude_unset=True).items():
            setattr(db_faculty, key, value)
        db.commit()
        db.refresh(db_faculty)
    return db_faculty

def delete_faculty(db: Session, faculty_id: int):
    db_faculty = get_faculty(db, faculty_id)
    if db_faculty:
        db.delete(db_faculty)
        db.commit()
    return db_faculty
