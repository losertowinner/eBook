import os.path as op
from sqlmodel import SQLModel, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base_dir = op.abspath(op.dirname(__file__))
db_name = "ebook.db"

SQLALCHEMY_DATABASE_URL = "sqlite:///" + op.join(base_dir, "database", db_name)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
