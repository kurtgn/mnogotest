from django.conf.urls import patterns, url,include
from core import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'datacenters', views.DataCenterViewSet)
router.register(r'floors', views.FloorViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'rows', views.RowViewSet)
router.register(r'racks', views.RackViewSet)
router.register(r'enclosures', views.EnclosureViewSet)
router.register(r'servertypes', views.ServerTypeViewSet)
router.register(r'servers', views.ServerViewSet)
router.register(r'cpus', views.CpuViewSet)
router.register(r'hdds', views.HddViewSet)
router.register(r'rams', views.RamViewSet)
router.register(r'raids', views.RaidViewSet)
router.register(r'nets', views.NetViewSet)




#router.register(r'enclosures', views.EnclosureViewSet)
urlpatterns = patterns(
    'core.views',
    url(r'', include(router.urls))
)