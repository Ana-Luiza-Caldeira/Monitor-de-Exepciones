from django.contrib import admin
from . import models

admin.site.register(models.Flow)
admin.site.register(models.Notification)
admin.site.register(models.OriginCon)
admin.site.register(models.DestinyCon)
admin.site.register(models.Data)
admin.site.register(models.Campo)
admin.site.register(models.Regras)