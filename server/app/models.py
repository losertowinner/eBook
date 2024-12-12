from sqlmodel import Field, Session, SQLModel, create_engine, select


class Common(SQLModel):
    id: int = Field(primary_key=True, index=True)
    is_active: bool = Field(default=True)


class Category(Common, table=True):
    title: str = Field(index=True, unique=True)
