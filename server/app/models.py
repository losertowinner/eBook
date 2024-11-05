from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    ForeignKey,
    Float,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base


class Common(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True)
    date_created = Column(DateTime, default=datetime.utcnow)


class Category(Common):
    __tablename__ = "category"

    name = Column(String(80), index=True, unique=True)
    books = relationship("Book", back_populates="category")

    def __str__(self):
        return self.name


class Book(Common):
    __tablename__ = "book"

    title = Column(String(100), index=True, unique=True)
    description = Column(Text, index=True)
    price = Column(Float, default=True)
    category_id = Column(Integer, ForeignKey("category.id"))

    category = relationship("Category", back_populates="books")

    def __str__(self):
        return self.title
