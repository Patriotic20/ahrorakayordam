from sqlalchemy import Column, Integer, String , Enum
from sqlalchemy.orm import relationship
from src.base.db import Base
import enum


class UserRole(enum.Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    
    student = relationship("Student", back_populates="user" , uselist=False)
    teacher = relationship("Teacher", back_populates="user" , uselist=False)
    