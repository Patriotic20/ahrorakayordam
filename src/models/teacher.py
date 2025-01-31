from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship
from src.base.db import Base


class Student(Base):
    __tablename__ = "teachers"
    user_id = Column(Integer, ForeignKey('users.id'))
    id = Column(Integer, primary_key=True)
    last_name = Column(String , nullable=True)
    first_name = Column(String , nullable=True)
    
    user = relationship('User', back_populates='teacher')