from app.middlewares.http import http

# Register middlewares by protocol here.
protocol_middlewares = {"http": http}

__all__ = ["protocol_middlewares"]
