from fastapi import APIRouter , Depends , HTTPException
from sqlalchemy.orm import Session 
from sqlalchemy.future import select
from src.base.db import get_db
from src.schemas.question import QuestionUpdate
from src.models.question import Question


router = APIRouter()


@router.put("/update-question")
def update_question(
    question_id : int,
    question_item: QuestionUpdate,
    db : Session = Depends(get_db)
):
    question = db.get(Question , question_id)
    if not question:
        raise HTTPException(
            status_code=404 , 
            detail="Question not found"
        )
    
    update_data = question_item.dict(exclude_unset=True)
    for key , value in update_data.items():
        setattr(question , key, value)
        
    db.commit()
    db.refresh(question)
    return question