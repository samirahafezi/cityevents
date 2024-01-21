from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Location

# Create your views here.

def home(request):
    return render(request, 'torontoevents/welcome.html', {'today': datetime.today()})

def list_locations_data(request):
    all_locations = Location.objects.all()
    return render(request, 'torontoevents/location_data_list.html', {'locations': all_locations})

@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'torontoevents/authorized.html', {})