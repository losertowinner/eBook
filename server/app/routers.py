from fastapi import APIRouter

from .schemas import Category
from .dao import load_categories

router = APIRouter(
    tags=["categories"],
)


@router.get("/categories", tags=["categories"], response_model=list[Category])
async def read_categories():
    return load_categories()
