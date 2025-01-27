from fastapi import APIRouter , Depends , UploadFile , File , HTTPException
from sqlalchemy.orm import Session
from src.base.db import get_db
from pathlib import Path
from src.models.question import Question

router = APIRouter()

@router.get("/")
def results(
    question : str,
    answer: str | None = None,
    db : Session = Depends(get_db)):

    user_test = db.query(Question).filter(Question.text == question).first()
    
    if user_test:
        if user_test.A == answer:
            return 1
    else:
        return 0
    