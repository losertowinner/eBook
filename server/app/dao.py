from sqlalchemy.orm import Session

from .models import Category, Book


def load_categories(db: Session):
    return db.query(Category).filter(Category.active.__eq__(True)).all()


def load_books(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(Book).filter(Book.active.__eq__(True)).offset(skip).limit(limit).all()
    )
