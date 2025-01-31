from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from src.base.db import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    science_teacher = Column(String, nullable=False)

    user = relationship('User', back_populates='teacher')