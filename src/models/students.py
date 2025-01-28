from sqlalchemy import Column, Integer, String, JSON

from src.base.db import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True)
    password = Column(String, nullable=True)
    test = Column(JSON)