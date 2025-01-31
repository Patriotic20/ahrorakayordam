from typing import Optional, Any, Dict
from pydantic import BaseModel

class StudentData(BaseModel):
    user_id : int
    last_name: str
    first_name: str

class StudentCreateRequest(StudentData):
    class Config:
        from_attributes = True

class StudentCreateResponse(StudentData):
    id : int
    class Config:
        from_attributes = True