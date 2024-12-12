from starlette_admin.contrib.sqla import Admin, ModelView

from .database import engine
from .models import Category

admin_manager = Admin(engine, title="eBook 🔖")
admin_manager.add_view(ModelView(Category))
