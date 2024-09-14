from app.middlewares.http.database import database_middleware
from app.middlewares.http.exception import exception_middleware

# Order of the middlewares is important.
http = [database_middleware, exception_middleware]

__all__ = ["http"]
