from fastapi import APIRouter , Depends , UploadFile , File , HTTPException
from sqlalchemy.orm import Session
from src.base.db import get_db
from pathlib import Path
from src.models.question import Question
from src.models.students import Student
from typing import List
from src.utils import  get_user_from_token

router = APIRouter()

@router.get("/")
def check_test(
    answers : List ,
    user_id : int = Depends(get_user_from_token) ,
    db: Session = Depends(get_db)):
    
    correct_count = 0
    incorrect_count = 0
    details = []
    
    for answer in answers:
        queston_text = answer.keys()
        question = next(iter(queston_text))
        question_from_db = db.query(Question).filter(Question.text == question)
        
         
    
    
