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