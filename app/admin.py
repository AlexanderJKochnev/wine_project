# app/admin.py
from fastapi import FastAPI
from sqladmin import Admin, ModelView
from app.database import engine
from app.models.users import User
from app.models.storage import Storage


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.username, User.surname, User.name]


class StorageAdmin(ModelView, model=Storage):
    column_list = [Storage.id, Storage.name, Storage.description]


def setup_admin(app: FastAPI):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(StorageAdmin)
