from pydantic import BaseModel
from typing import Optional

    
class QuestionBase(BaseModel):
    text: str
    A: str 
    B: str 
    C: str 
    D: str 
    



class QuestionUpdate(BaseModel):
    text : Optional[str] = None
    B: Optional[str] = None
    A: Optional[str] = None
    C: Optional[str] = None
    D: Optional[str] = None
    
class QuestionResponse(QuestionBase):
    id : int
    
    class Config:
        from_attributes = True