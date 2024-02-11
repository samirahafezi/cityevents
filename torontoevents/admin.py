from django.contrib import admin

from . import models

class LocationAdmin(admin.ModelAdmin):
    list_display = ('location_address','longtitude', 'latitude',)

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_id', 'location_id', 'facility_display_name', 'permit', 'facility_type', 'facility_rating', 'asset_name')

class RegisteredProgramAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'location_id', 'activity_title', 'course_title', 'activity_description')

class DropInProgramAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'location_id', 'course_title', 'date_range', 'category')


admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Facility, FacilityAdmin)
admin.site.register(models.RegisteredProgram, RegisteredProgramAdmin)
admin.site.register(models.DropInProgram, DropInProgramAdmin)