from pydantic import BaseModel


class TeacherData(BaseModel):
    first_name: str
    last_name: str
    contact: str
    science_teacher: str

class TeacherCreateRequest(TeacherData):
    class Config:
        from_attributes = True

class TeacherCreateResponse(TeacherData):
    id : int
    class Config:
        from_attributes = True