from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import urllib.parse

password = urllib.parse.quote_plus("Nikhil@123")

engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/aichatbot_db")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()