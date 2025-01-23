from sqlalchemy import Column , Integer , String , Text, ForeignKey
from sqlalchemy.orm import relationship
from src.base.db import Base

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer , primary_key=True, nullable=False)
    text = Column(String , nullable=False)
    is_correct = Column(Integer, nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    
    question = relationship("Question", back_populates="answers")