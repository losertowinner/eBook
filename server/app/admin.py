from sqladmin import ModelView

from .models import Category, Book


class BaseAdmin(ModelView, model=None):
    column_list = ["active", "date_created"]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True
    page_size = 50
    page_size_options = [25, 50, 100, 200]
    column_sortable_list = ["id"]


class CategoryAdmin(BaseAdmin, model=Category):
    name_plural = "Categories"
    column_list = [Category.name] + BaseAdmin.column_list
    column_searchable_list = [Category.name]


class BookAdmin(BaseAdmin, model=Book):
    column_list = [Book.title, Book.price, Book.category] + BaseAdmin.column_list
    column_searchable_list = [Book.title]
