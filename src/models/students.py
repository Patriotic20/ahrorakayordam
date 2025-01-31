from sqlalchemy import Column, Integer, String, JSON , ForeignKey
from sqlalchemy.orm import relationship

from src.base.db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    last_name = Column(String , nullable=True)
    first_name = Column(String , nullable=True)
    
    user = relationship("User" , back_populates="student")
    
    # test_result = Column(JSON)
    # correct_answers = Column(Integer , nullable=True)
    # incorrect_answers = Column(Integer , nullable=True)