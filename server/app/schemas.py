from pydantic import BaseModel


class CommonInfo(BaseModel):
    id: int
    active: bool


class Category(CommonInfo):
    name: str

    class Config:
        orm_mode = True


class Book(CommonInfo):
    title: str
    description: str | None = None
    price: float
    category_id: int

    class Config:
        orm_mode = True
