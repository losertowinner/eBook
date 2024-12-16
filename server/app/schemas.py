from pydantic import BaseModel


class Common(BaseModel):
    id: int
    is_active: bool


class Base(BaseModel):
    title: str


class Category(Common):
    title: str


class Book(Common):
    title: str
    description: str
    price: float
