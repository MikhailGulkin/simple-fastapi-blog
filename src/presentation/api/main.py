import uvicorn
from fastapi import FastAPI

from src.config import get_settings
from src.dal.db.main import create_engine, build_sessions
from .controllers import setup_controllers
from .dependency_injection import setup_di


def build_app() -> FastAPI:
    app = FastAPI()
    settings = get_settings()

    setup_di(
        app,
        build_sessions(create_engine(settings.DB_URL))
    )

    setup_controllers(app.router)

    return app


if __name__ == '__main__':
    uvicorn.run(
        app="src.presentation.api.main:build_app",
        factory=True,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
