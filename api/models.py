from mongoengine import fields, Document


class User(Document):

  id = fields.ObjectId()
  username = fields.StringField(required=True, max_length=100)
  email = fields.EmailField(required=True)
  first_name = fields.StringField(required=True, max_length=100)
  last_name = fields.StringField(required=True, max_length=100)


class Asset(Document):

  id = fields.ObjectId()
  name = fields.StringField(required=True, max_length=100)
  description = fields.StringField(required=True, max_length=500)
  created = fields.DateTimeField(required=True)


class Scan(Document):

  id = fields.ObjectId()
  requested_by = fields.IntField(required=True)
  started_at = fields.DateTimeField(required=True)
  finished_at = fields.DateTimeField(required=True)
  name = fields.StringField(required=True, max_length=100)
  status = fields.StringField(required=True, max_length=100)
  scanners = fields.ListField(required=True)
  severity_counts = fields.DictField(required=True)
  assets_scanned = fields.ListField(required=True)


class Vulnerability(Document):

  id = fields.ObjectId()
  from_scan = fields.IntField(required=True)
  severity = fields.StringField(required=True, max_length=100)
  name = fields.StringField(required=True, max_length=100)
  description = fields.StringField(required=True, max_length=1000)
  solution = fields.StringField(required=True, max_length=1000)
  references = fields.StringField(required=True, max_length=1000)
  cvss_base_score = fields.FloatField(required=True)
  affected_assets = fields.ListField(required=True)
