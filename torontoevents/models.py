from django.db import models
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
import csv

class Location(models.Model):
    location_id = models.IntegerField(null=False)
    location_address = models.CharField(max_length=300)
    longtitude = models.FloatField(default=None, blank=True, null=True)
    latitude = models.FloatField(default=None, blank=True, null=True)
    centreline_type = models.CharField(max_length=300, default=None, blank=True, null=True)
    centreline_id = models.CharField(max_length=300, default=None, blank=True, null=True)
    px = models.CharField(max_length=300, default=None, blank=True, null=True)
    latest_count_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True) #auto populate the date to now

    # def __str__(self):
    #     return self.name

    def load_locations_data():
        #loop through the csv file line by line
        with open("torontoevents/files/Locations.csv", "r") as file:
            next(file) #skip header line
            for item in file:
                if not item:
                    break

                #extract each entry into its own field
                location_line = item.split(',')
                
                # printing the list using loop
                # print(*location_line, sep = ", ")

                location_count = Location.objects.filter(location_id=int(location_line[1])).count()
                if location_count > 0:
                    Location.objects.filter(location_id=int(location_line[1])).update(
                        location_id=location_line[1], 
                        location_address=location_line[2], 
                        longtitude = location_line[3], 
                        latitude = location_line[4], 
                        centreline_type = location_line[5], 
                        centreline_id = location_line[6], 
                        px = location_line[7], 
                        latest_count_date = location_line[8], 
                    )
                else:
                    Location.objects.create(
                        location_id=location_line[1], 
                        location_address=location_line[2], 
                        longtitude = location_line[3], 
                        latitude = location_line[4], 
                        centreline_type = location_line[5], 
                        centreline_id = location_line[6], 
                        px = location_line[7], 
                        latest_count_date = location_line[8], 
                    )

        file.closed


class Facility(models.Model):
    facility_id = models.IntegerField(null=False)
    location_id = models.IntegerField(null=False)
    facility_display_name = models.CharField(max_length=300, default=None, blank=True, null=True)
    permit = models.CharField(max_length=100, default=None, blank=True, null=True)
    facility_type = models.CharField(max_length=300, default=None, blank=True, null=True)
    facility_rating = models.CharField(max_length=100, default=None, blank=True, null=True)
    asset_name = models.CharField(max_length=300, default=None, blank=True, null=True)

    # def __str__(self):
    #     return self.name
    
    def load_facilities_data():
        #loop through the csv file line by line
        with open("torontoevents/files/Facilities.csv", "r") as file:
            next(file) #skip header line
            for item in file:
                if not item:
                    break

                #extract each entry into its own field
                facility_line = item.split(',')
                
                # printing the list using loop
                # print(*facility_line, sep = ", ")

                facility_count = Facility.objects.filter(facility_id=int(facility_line[1])).count()
                if facility_count > 0:
                    Facility.objects.filter(facility_id=int(facility_line[1])).update(
                        facility_id=facility_line[1], 
                        location_id=facility_line[2], 
                        facility_display_name = facility_line[3], 
                        permit = facility_line[4], 
                        facility_type = facility_line[5], 
                        facility_rating = facility_line[6], 
                        asset_name = facility_line[7], 
                    )
                else:
                    Facility.objects.create(
                        facility_id=facility_line[1], 
                        location_id=facility_line[2], 
                        facility_display_name = facility_line[3], 
                        permit = facility_line[4], 
                        facility_type = facility_line[5], 
                        facility_rating = facility_line[6], 
                        asset_name = facility_line[7], 
                    )

        file.closed