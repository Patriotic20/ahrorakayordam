from sqlalchemy import Column, Integer, String, JSON
from src.api.question_bank.random_choose import get_test

from src.base.db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    test = Column(JSON)