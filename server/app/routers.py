from fastapi import APIRouter

from .schemas import Category, Book
from .dao import select_categories, select_books, select_book

categories_router = APIRouter(
    tags=["categories"],
)

books_router = APIRouter(
    tags=["books"],
)


@categories_router.get(
    "/categories", tags=["categories"], response_model=list[Category]
)
async def read_categories():
    return select_categories()


@books_router.get("/books", tags=["books"], response_model=list[Book])
async def read_books():
    return select_books()


@books_router.get("/books/{id}", tags=["books"], response_model=Book)
async def read_book(id: int):
    return select_book(id=id)
