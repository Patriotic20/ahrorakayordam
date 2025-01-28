from fastapi import APIRouter , Depends , UploadFile , File , HTTPException
from sqlalchemy.orm import Session
from src.base.db import get_db
from pathlib import Path
from src.models.question import Question
from src.utils import  get_user_from_token

router = APIRouter()

@router.get("/")
def results(
    question : str,
    answer: str | None = None,
    user_id : int = Depends(get_user_from_token),
    db : Session = Depends(get_db)):
    
    user_test = db.query(Question).filter(Question.text == question).first()
    
    if user_test:
        if user_test.A == answer:
            return 1
    else:
        return 0
    