from sqladmin import ModelView

from src.infrastructure.db.models import User


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.username,
        User.email,
        User.password,
    ]

    def __str__(self):
        return f'{User.id} - {User.username}'
