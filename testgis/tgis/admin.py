from django.contrib import admin

from django.contrib.gis import admin
from . import models

class LocationAdmin(admin.GeoModelAdmin):

 search_fields = ['name','uuid']
 list_display = ['uuid','name','point',]
 readonly_fields = ['uuid','slug',]

admin.site.register(models.Location, LocationAdmin)

class RegionAdmin(admin.GeoModelAdmin):

 search_fields = ['name','uuid']
 list_display = ['uuid','name']

admin.site.register(models.Region, RegionAdmin)

# Register your models here.
