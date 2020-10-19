from django.contrib import admin
from django.urls import include, path, re_path

from vessel_api.vessels.routers import router as vessel_router
from vessel_api.vessels.routers import equipments_router

from .schema import schema_view

urlpatterns = [
	re_path(r'^$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),

    path('', include(vessel_router.urls)),
    path('', include(equipments_router.urls)),
]
