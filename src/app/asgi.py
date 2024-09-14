"""
ASGI setup for project.

It exposes the ASGI callable as a module-level variable named ``application``.
"""

from fastapi import FastAPI

from app import settings
from app.ext.lifespan import lifespan
from app.middlewares import protocol_middlewares
from app.urls import urlpatterns


def get_asgi_application() -> FastAPI:
    """
    Generate an application to be used by an ASGI server.
    :return: app, FastAPI
    """
    app = FastAPI(lifespan=lifespan, **settings.OPENAPI)

    # Register middlewares.
    for protocol, middlewares in protocol_middlewares.items():
        for middleware in middlewares:
            app.middleware(protocol)(middleware)

    # Register routers.
    for router in urlpatterns:
        app.include_router(router)

    return app


application = get_asgi_application()
