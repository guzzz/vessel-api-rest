from rest_framework_nested import routers

from . import views
from vessel_api.equipments.views import InactivateEquipmentViewSet, EquipmentModelViewSet


router = routers.DefaultRouter()
router.register(r'vessels', views.VesselModelViewSet)
router.register(r'inactivate-equipments', InactivateEquipmentViewSet)

equipments_router = routers.NestedSimpleRouter(
    parent_router=router,
    parent_prefix=r'vessels',
    lookup='vessel'
)

equipments_router.register(
    prefix=r'equipments',
    viewset=EquipmentModelViewSet
)
