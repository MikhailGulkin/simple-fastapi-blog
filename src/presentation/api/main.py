import uvicorn
from fastapi import FastAPI

from .controllers import setup_controllers
from .dependency_injection import setup_di


def build_app() -> FastAPI:
    app = FastAPI()

    setup_di(app)
    setup_controllers(app.router)

    return app


if __name__ == '__main__':
    uvicorn.run(
        app="src.presentation.api.main:build_app",
        factory=True,
        host="0.0.0.0",
        reload=True
    )
