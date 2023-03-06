from sqladmin import ModelView

from src.infrastructure.db.models import Post


class PostAdmin(ModelView, model=Post):
    column_list = [
        Post.id,
        Post.author_id,
        Post.title,
        Post.summary,
        Post.body,
        Post.published_at
    ]
