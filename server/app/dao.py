from sqlmodel import select, Session

from .models import Category, Book
from .database import engine


def select_categories() -> list[Category]:
    with Session(engine) as session:
        return session.exec(select(Category).where(Category.is_active == True)).all()


def select_books() -> list[Book]:
    with Session(engine) as session:
        return session.exec(select(Book).where(Book.is_active == True)).all()


def select_book(id: int) -> Book:
    with Session(engine) as session:
        return session.get(Book, id)
