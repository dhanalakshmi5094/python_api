from django_mongoengine import mongo_admin as admin
from .models import User , Asset, Scan , Vulnerability
from django_mongoengine import document
# Register your models here.


admin.site.register(User)
admin.site.register(Asset)
admin.site.register(Scan)
admin.site.register(Vulnerability)
