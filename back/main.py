from fastapi import FastAPI

from routers.user_router import user_router


def create_app() -> FastAPI:
    new_app = FastAPI(
        title='Test app',
        version='0.0.1a'
    )

    new_app.include_router(user_router)

    return new_app


app = create_app()
