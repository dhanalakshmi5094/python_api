from rest_framework_mongoengine import viewsets
from .serializers import UserSerializer, AssetSerializer, ScanSerializer, VulnerabilitySerializer
from .models import User as User, Asset, Scan, Vulnerability


class UserViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer


class AssetViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Asset.objects.all()
  serializer_class = AssetSerializer


class ScanViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Scan.objects.all()
  serializer_class = ScanSerializer


class VulnerabilityViewSet(viewsets.ReadOnlyModelViewSet):
  queryset = Vulnerability.objects.all()
  serializer_class = VulnerabilitySerializer
