from pydantic import BaseModel

class DepartmentBase(BaseModel):
    name: str
    description: str | None = None
    faculty_id: int

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(DepartmentBase):
    pass
