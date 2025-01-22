
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from .config import settings

engine = create_engine(settings.connection_string, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

class Base(DeclarativeBase):
    pass
