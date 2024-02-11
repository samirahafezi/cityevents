from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Location
from .models import Facility
from .models import RegisteredProgram
from .models import DropInProgram

# Create your views here.

def home(request):
    return render(request, 'torontoevents/welcome.html', {'today': datetime.today()})

def list_locations_data(request):
    all_locations = Location.objects.all()
    return render(request, 'torontoevents/location_data_list.html', {'locations': all_locations})

def list_facilities_data(request):
    all_facilities = Facility.objects.all()
    return render(request, 'torontoevents/facility_data_list.html', {'facilities': all_facilities})

def list_registered_programs_data(request):
    all_registered_programs = RegisteredProgram.objects.all()
    return render(request, 'torontoevents/registered_program_data_list.html', {'registered_programs': all_registered_programs})

def list_dropin_programs_data(request):
    all_dropin_programs = DropInProgram.objects.all()
    return render(request, 'torontoevents/dropin_program_data_list.html', {'dropin_programs': all_dropin_programs})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'torontoevents/authorized.html', {})