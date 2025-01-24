from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session 
from src.models.question import Question
from src.base.db import get_db
import random

router = APIRouter()


@router.get("/random-choose")
def get_test(db : Session = Depends(get_db)):
    db_content = db.query(Question).all()
    if not db_content:
        return {"error": "No questions available"}
    

    num_questions_to_select = min(25, len(db_content))
    

    random_questions = random.sample(db_content, num_questions_to_select)
    
    return random_questions
