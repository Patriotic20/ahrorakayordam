from sqlalchemy import Column , Integer , String , Text, ForeignKey 
from sqlalchemy.orm import relationship
from src.base.db import Base

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer , primary_key=True , nullable=False)
    text = Column(Text , nullable=False)
    imgae = Column(String , nullable=True)
    
    answers = relationship("Answer", back_populates="question", cascade="all, delete")