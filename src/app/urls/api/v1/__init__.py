from fastapi import APIRouter

from app.urls.api.v1.hello import hello

urlpatterns = [hello]

v1 = APIRouter(prefix="/api")
for router in urlpatterns:
    v1.include_router(router)

__all__ = ["v1"]
