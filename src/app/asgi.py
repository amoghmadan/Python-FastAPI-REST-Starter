from fastapi import FastAPI

from app import settings
from app.ext.lifespan import lifespan
from app.middlewares import database_middleware, exception_middleware
from app.urls import urlpatterns


def get_asgi_application():
    app = FastAPI(lifespan=lifespan, **settings.OPENAPI)

    http_middlewares = [database_middleware, exception_middleware]
    for middleware in http_middlewares:
        app.middleware("http")(middleware)

    for router in urlpatterns:
        app.include_router(router)

    return app


application = get_asgi_application()
