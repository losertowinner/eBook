from os import path
from typing import Annotated
from fastapi import Depends
from sqlmodel import Field, Session, SQLModel, create_engine

from .models import Category, Book

base_dir = path.abspath(path.dirname(__file__))
sqlite_file_name = "ebook.db"
sqlite_url = "sqlite:///" + path.join(base_dir, "database", sqlite_file_name)

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def seed_data():
    with Session(engine) as session:
        category_news = Category(title="News")

        book_deadpond = Book(
            title="Deadpond",
            description="Deadpond with me",
            price=33.99,
            category=category_news,
        )
        book_doraemon = Book(
            title="Doraemon",
            description="Doraemnon with me",
            price=133.99,
            category=category_news,
        )

        session.add(category_news)
        session.add_all([book_deadpond, book_doraemon])
        session.commit()


SessionDep = Annotated[Session, Depends(get_session)]
