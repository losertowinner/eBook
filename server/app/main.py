from fastapi import FastAPI
from sqladmin import Admin

from . import models
from .database import engine
from .controllers import router
from .admin import CategoryAdmin, BookAdmin

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="eBook 🔖",
    description="APIs for eBook 🎉",
    openapi_version="1.0.0",
    debug=True,
    docs_url="/",
    terms_of_service="https://fastevent.com/terms",
    contact={
        "name": "Support",
        "url": "http://github.com/losertowinner",
        "email": "zin.it.dev@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    openapi_tags=[
        {
            "name": "categories",
            "description": "🎨 Operations with categories, including retrieving and managing book categories",
        },
        {"name": "books", "description": "🎪 Operations related to books management"},
    ],
)
app.include_router(router)

admin = Admin(app, engine, title="eBook 🔖")
admin.add_view(CategoryAdmin)
admin.add_view(BookAdmin)
