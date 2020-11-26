from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, AssetViewSet, ScanViewSet, VulnerabilityViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="User")
router.register(r'assets', AssetViewSet, basename="Asset")
router.register(r'scans', ScanViewSet, basename="Scan")
router.register(r'vulnerabilities', VulnerabilityViewSet, basename="Vulnerability")

urlpatterns = [
  url('', include(router.urls)),
]
