from fastapi import APIRouter , Depends , UploadFile , File , HTTPException
from sqlalchemy.orm import Session
from src.base.db import get_db
from pathlib import Path
from src.models.question import Question
import shutil


router = APIRouter()

UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True) 


@router.put("/upload/image/{id}")
def upload_image(
    id : int,
    file: UploadFile = File(...), 
    db : Session = Depends(get_db)):
    
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400, 
            detail="File is not an image."
        )
    
    question = db.query(Question).filter(Question.id == id).first()
    if not question:
        raise HTTPException(
            status_code=404, 
            detail="Question not found.")
    
    try:
        image_path = UPLOAD_DIR / file.filename
        
        with image_path.open("wb") as buffer:
            shutil.copyfileobj(file.file , buffer)
        
        question.imgae = str(image_path)
        db.commit()
        db.refresh(question)
        
        return {
            "message": "Image added successfully",
            "question_id": question.id,
            "image_path": question.imgae,
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to upload image: {str(e)}")
