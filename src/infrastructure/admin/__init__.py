from sqladmin import Admin

from src.infrastructure.admin.models.post import PostAdmin
from src.infrastructure.admin.models.user import UserAdmin


def setup_admin_models(admin_app: Admin) -> None:
    for app in [
        PostAdmin,
        UserAdmin
    ]:
        admin_app.add_view(app)

