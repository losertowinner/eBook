from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import create_db_and_tables, SessionDep, seed_data
from .models import Category
from .routers import categories_router, books_router
from .admin import admin_manager


tags_metadata = [
    {"name": "categories", "description": "Categories operations"},
    {"name": "books", "description": "Books operations"},
]

app = FastAPI(
    docs_url="/",
    title="eBook 🔖 - Swagger UI",
    description="Documents API for eBook 📖",
    summary="An API for efficiently managing and sharing eBooks 📚",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "ZIN",
        "url": "https://github.com/losertowinner/",
        "email": "zin.it.dev@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=tags_metadata,
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories_router)
app.include_router(books_router)

admin_manager.mount_to(app)


def main():
    create_db_and_tables()
    seed_data()


if __name__ == "__main__":
    main()
