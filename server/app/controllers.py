from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .dao import load_categories, load_books
from .schemas import Category, Book
from .database import get_db

router = APIRouter()


@router.get("/categories", tags=["categories"], response_model=list[Category])
async def categories(db: Session = Depends(get_db)):
    return load_categories(db)


@router.get("/books", tags=["books"], response_model=list[Book])
async def books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return load_books(db, skip=skip, limit=limit)
