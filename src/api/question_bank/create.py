from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from src.base.db import get_db
from src.schemas.question import QuestionBase
from src.models.question import Question


router = APIRouter()


@router.post("/create-question")
def create_question(
    question_item: QuestionBase, 
    db: Session = Depends(get_db)):
    quiz = Question(**question_item.model_dump(exclude_unset=True))
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz
    ...