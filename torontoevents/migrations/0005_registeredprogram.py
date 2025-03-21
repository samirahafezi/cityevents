# Generated by Django 5.0.1 on 2024-02-02 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torontoevents', '0004_alter_facility_location_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisteredProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('location_id', models.IntegerField()),
                ('activity_title', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('course_title', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('activity_description', models.CharField(blank=True, default=None, max_length=3000, null=True)),
                ('days_of_the_week', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('from_to_dates', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('start_hour', models.IntegerField()),
                ('start_min', models.IntegerField()),
                ('end_hour', models.IntegerField()),
                ('end_min', models.IntegerField()),
                ('start_date', models.DateField()),
                ('efun_url', models.URLField()),
                ('min_age', models.IntegerField()),
                ('max_age', models.IntegerField()),
                ('program_category', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('registration_date', models.DateField()),
                ('status_information', models.CharField(blank=True, default=None, max_length=300, null=True)),
            ],
        ),
    ]
