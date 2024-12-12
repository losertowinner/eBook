from .models import Category
from .database import engine

from sqlmodel import select, Session


def load_categories() -> list[Category]:
    with Session(engine) as session:
        statement = select(Category).where(Category.is_active == True)
        categories = session.exec(statement).all()
    return categories
