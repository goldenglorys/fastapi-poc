from app.api.health.routes import router as health_router
from app.api.v1.routes import router as v1_router
from fastapi import APIRouter, FastAPI


def create_app() -> FastAPI:
    """Create and configure a FastAPI application instance.

    This function sets up a FastAPI application instance with the specified description and title.
    It then creates an APIRouter instance with a tag "Root" and includes the `health_router` and
    `v1_router` routers into the main FastAPI application instance.

    Returns:
        FastAPI: The configured FastAPI application instance.
    """
    app = FastAPI()

    router = APIRouter()

    router.include_router(health_router)

    app.include_router(router)

    app.include_router(v1_router)

    return app
