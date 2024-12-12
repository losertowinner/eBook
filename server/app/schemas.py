from pydantic import BaseModel


class Common(BaseModel):
    id: int
    is_active: bool


class Category(Common):
    title: str
