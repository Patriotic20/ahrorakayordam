from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy.future import select
from src.base.db import get_db
from src.models.question import Question
from src.models.students import Student
from typing import Dict
from src.utils import  get_user_from_token

router = APIRouter()

@router.get("/test-check")
def check_test(
    answers: Dict[str , str],
    user_id: int = Depends(get_user_from_token),
    db: Session = Depends(get_db)):
    
    question_texts = list(answers.keys())
    question_query = db.execute(select(Question).where(Question.text.in_(question_texts)))
    questions = {q.text: q.A for q in question_query.scalars().all()}
    
    correct_count = sum(1 for q_text , answer in answers.items() if questions.get(q_text) == answer)
    incorrect_count = len(answers) - correct_count
    
    user = db.execute(select(Student).where(Student.id == user_id)).scalars().first()
    if not user:
        raise HTTPException(status_code=404 , detail="User not found")
    
    user.test = answers
    user.correct_answers = correct_count
    user.incorrect_answers = incorrect_count
    
    db.commit()
    db.refresh(user)
    return user
    