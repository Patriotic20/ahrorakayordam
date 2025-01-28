from pydantic import BaseModel

class FacultyBase(BaseModel):
    name: str
    description: str | None = None

class FacultyCreate(FacultyBase):
    pass

class FacultyUpdate(FacultyBase):
    pass
