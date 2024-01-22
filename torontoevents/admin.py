from django.contrib import admin

from . import models

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_address','longtitude', 'latitude',)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_id', 'location_id', 'facility_display_name', 'permit', 'facility_type', 'facility_rating', 'asset_name')

admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Facility, FacilityAdmin)