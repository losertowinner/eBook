from sqlmodel import Field, Session, Relationship, SQLModel, create_engine, select


class Common(SQLModel):
    id: int = Field(primary_key=True, index=True)
    is_active: bool = Field(default=True)


class Category(Common, table=True):
    title: str = Field(index=True, unique=True)

    books: list["Book"] = Relationship()


class Book(Common, table=True):
    title: str = Field(index=True, unique=True)
    description: str
    price: float = Field(default=0.00)

    categorycategory_id: int | None = Field(default=None, foreign_key="category.id")
    category: Category | None = Relationship(back_populates="books")
