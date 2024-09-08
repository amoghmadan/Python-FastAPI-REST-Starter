from fastapi import APIRouter

from app.urls.api.v1 import v1

urlpatterns = [v1]

api = APIRouter(prefix="/api")
for router in urlpatterns:
    api.include_router(router)

__all__ = ["api"]
