from django.db import models
from django.contrib import admin

class ushort(models.Model):
    longurl=models.URLField()
    shorturl=models.URLField()
admin.site.register(ushort)