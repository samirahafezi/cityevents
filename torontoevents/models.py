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


class RegisteredProgram(models.Model):
    course_id = models.IntegerField(null=False)
    location_id = models.IntegerField(null=False)
    activity_title = models.CharField(max_length=300, default=None, blank=True, null=True)
    course_title = models.CharField(max_length=300, default=None, blank=True, null=True)
    activity_description = models.CharField(max_length=3000, default=None, blank=True, null=True)
    days_of_the_week = models.CharField(max_length=50, default=None, blank=True, null=True)
    from_to_dates = models.CharField(max_length=300, default=None, blank=True, null=True)
    start_hour = models.IntegerField()
    start_min = models.IntegerField()
    end_hour = models.IntegerField()
    end_min = models.IntegerField()
    start_date = models.DateField()
    efun_url = models.URLField()
    min_age = models.CharField(max_length=50, default=None, blank=True, null=True)
    max_age = models.CharField(max_length=50, default=None, blank=True, null=True)
    program_category = models.CharField(max_length=300, default=None, blank=True, null=True)
    registration_date = models.DateField()
    status_information = models.CharField(max_length=300, default=None, blank=True, null=True)

    def load_registered_programs_data():
        #loop through the csv file line by line
        with open("torontoevents/files/Registered Programs.csv", "r") as file:
            next(file) #skip header line
            for line in file:
                if not line:
                    break

                csv_data = line
                reader = csv.reader([csv_data])
                fields = next(reader)
                # print("Processing: "+fields[1])

                program_count = RegisteredProgram.objects.filter(course_id=int(fields[1])).count()
                if program_count > 0:
                    RegisteredProgram.objects.filter(course_id=int(fields[1])).update(
                    course_id=fields[1],
                    location_id=fields[2],
                    activity_title=fields[3],
                    course_title=fields[4],
                    activity_description=fields[5],
                    days_of_the_week=fields[6],
                    from_to_dates=fields[7],
                    start_hour=fields[8],
                    start_min=fields[9],
                    end_hour=fields[10],
                    end_min=fields[11],
                    start_date=fields[12],
                    efun_url=fields[13],
                    min_age=fields[14],
                    max_age=fields[15],
                    program_category=fields[16],
                    registration_date=fields[17],
                    status_information=fields[18],
                    )
                else:
                    RegisteredProgram.objects.create(
                        course_id=fields[1],
                        location_id=fields[2],
                        activity_title=fields[3],
                        course_title=fields[4],
                        activity_description=fields[5],
                        days_of_the_week=fields[6],
                        from_to_dates=fields[7],
                        start_hour=fields[8],
                        start_min=fields[9],
                        end_hour=fields[10],
                        end_min=fields[11],
                        start_date=fields[12],
                        efun_url=fields[13],
                        min_age=fields[14],
                        max_age=fields[15],
                        program_category=fields[16],
                        registration_date=fields[17],
                        status_information=fields[18],
                    )

        file.closed    


class DropInProgram(models.Model):
    location_id = models.IntegerField(null=False)
    course_id = models.IntegerField(null=False)
    course_title = models.CharField(max_length=300, default=None, blank=True, null=True)
    min_age = models.CharField(max_length=50, default=None, blank=True, null=True)
    max_age = models.CharField(max_length=50, default=None, blank=True, null=True)
    date_from = models.CharField(max_length=50, default=None, blank=True, null=True)
    date_range = models.CharField(max_length=3000, default=None, blank=True, null=True)
    start_date_time = models.DateTimeField()
    start_hour = models.IntegerField()
    start_min = models.IntegerField()
    end_hour = models.IntegerField()
    end_min = models.IntegerField()
    category = models.CharField(max_length=300, default=None, blank=True, null=True)
    first_date = models.DateTimeField()
    last_date = models.DateTimeField()

    def load_drop_in_programs_data():
        #loop through the csv file line by line
        with open("torontoevents/files/Drop-in.csv", "r") as file:
            next(file) #skip header line
            for line in file:
                if not line:
                    break

                csv_data = line
                reader = csv.reader([csv_data])
                fields = next(reader)
                print("Processing: "+fields[1])

                program_count = DropInProgram.objects.filter(location_id=int(fields[1]), 
                                                             course_id=int(fields[2]),
                                                             date_range=fields[7]).count()
                # DropInProgram.objects.filter(location_id=7, course_id=7479091, date_range='Dec 31 to Jan 6')
                if program_count > 0:
                    DropInProgram.objects.filter(location_id=int(fields[1]), 
                                                 course_id=int(fields[2]),
                                                 date_range=fields[7]).update(
                    location_id = fields[1],
                    course_id = fields[2],
                    course_title = fields[3],
                    min_age = fields[4],
                    max_age = fields[5],
                    date_from = fields[6],
                    date_range = fields[7],
                    start_date_time = fields[8],
                    start_hour = fields[9],
                    start_min = fields[10],
                    end_hour = fields[11],
                    end_min = fields[12],
                    category = fields[13],
                    first_date = fields[14],
                    last_date = fields[15],
                )
                else:
                    DropInProgram.objects.create(
                    location_id = fields[1],
                    course_id = fields[2],
                    course_title = fields[3],
                    min_age = fields[4],
                    max_age = fields[5],
                    date_from = fields[6],
                    date_range = fields[7],
                    start_date_time = fields[8],
                    start_hour = fields[9],
                    start_min = fields[10],
                    end_hour = fields[11],
                    end_min = fields[12],
                    category = fields[13],
                    first_date = fields[14],
                    last_date = fields[15],
                )

        file.closed    
