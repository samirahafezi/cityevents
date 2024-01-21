from django.contrib import admin

from . import models

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_address','longtitude', 'latitude',)
    
admin.site.register(models.Location, LocationAdmin)