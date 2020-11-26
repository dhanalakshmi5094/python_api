from rest_framework import fields
from .models import User, Asset, Scan, Vulnerability
from rest_framework_mongoengine import serializers


class UserSerializer(serializers.DocumentSerializer):
  id = fields.IntegerField(required=True)
  username = fields.CharField(required=True)
  email = fields.EmailField(required=True)
  first_name = fields.CharField(required=True)
  last_name = fields.CharField(required=True)

  class Meta:
    model = User
    fields = '__all__'


class AssetSerializer(serializers.DocumentSerializer):
  id = fields.IntegerField(required=True)
  name = fields.CharField(required=True)
  description = fields.CharField(required=True)
  created = fields.DateTimeField(required=True)

  class Meta:
    model = Asset
    fields = '__all__'


class ScanSerializer(serializers.DocumentSerializer):
  id = fields.IntegerField(required=True)
  requested_by = fields.IntegerField(required=True)
  started_at = fields.DateTimeField(required=True)
  finished_at = fields.DateTimeField(required=True)
  name = fields.CharField(required=True)
  status = fields.CharField(required=True)
  scanners = fields.ListField(required=True)
  severity_counts = fields.DictField(required=True)
  assets_scanned = fields.ListField(required=True)

  class Meta:
    model = Scan
    fields = '__all__'


class VulnerabilitySerializer(serializers.DocumentSerializer):
  id = fields.IntegerField(required=True)
  from_scan = fields.IntegerField(required=True)
  severity = fields.CharField(required=True)
  name = fields.CharField(required=True)
  description = fields.CharField(required=True)
  solution = fields.CharField(required=True)
  references = fields.CharField(required=True)
  cvss_base_score = fields.FloatField(required=True)
  affected_assets = fields.ListField(required=True)

  class Meta:
    model = Vulnerability
    fields = '__all__'
