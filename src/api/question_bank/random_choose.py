from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session 
from src.models.question import Question
from src.base.db import get_db
from src.schemas.question import QuestionResponse
from typing import List
import random

router = APIRouter()


@router.get("/random-choose" , response_model=List[QuestionResponse])
def get_test(db : Session = Depends(get_db)):
    db_content = db.query(Question).all()
    if not db_content:
        return {"error": "No questions available"}
    

    num_questions_to_select = min(25, len(db_content))
    

    random_questions = random.sample(db_content, num_questions_to_select)
    
    for question in  random_questions:
        varants = [question.A , question.B , question.C , question.D]
        random.shuffle(varants)
        question.A , question.B , question.C , question.D = varants
        
    
    return [QuestionResponse(**question.__dict__) for question in random_questions]
