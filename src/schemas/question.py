from pydantic import BaseModel
from typing import Optional

class QuestionResponse(BaseModel):
    text : str
    image : Optional[str] = None
    A: str 
    B: str 
    C: str 
    D: str 