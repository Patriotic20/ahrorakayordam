from typing import Optional, Any, Dict
from pydantic import BaseModel

class StudentData(BaseModel):
    username: str
    password: str
    test: Optional[Dict[str, Any]] = None

class StudentCreateRequest(StudentData):
    class Config:
        from_attributes = True

class StudentCreateResponse(StudentData):
    id : int
    class Config:
        from_attributes = True