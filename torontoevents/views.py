from django.shortcuts import render
from datetime import datetime
from .models import Location
from .models import Facility
from .models import RegisteredProgram
from .models import DropInProgram
from django.http import Http404
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from itertools import chain

class HomeView(TemplateView):
    template_name = 'torontoevents/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'torontoevents/authorized.html'
    login_url = '/admin'

class LocationsListView(ListView):
    model = Location
    context_object_name = "locations"
    template_name = 'torontoevents/location_data_list.html'

class FacilitiesListView(ListView):
    model = Facility
    context_object_name = "facilities"
    template_name = 'torontoevents/facility_data_list.html'

class RegisteredProgramsListView(ListView):
    model = RegisteredProgram
    context_object_name = "registered_programs"
    template_name = 'torontoevents/registered_program_data_list.html'

class RegisteredProgramDetailView(DetailView):
    model = RegisteredProgram
    context_object_name = "registered_program"
    template_name = 'torontoevents/registered_program_detail.html'

# def registered_program_detail(request, id):
#     try:
#         registered_program = RegisteredProgram.objects.get(id=id)
#     except RegisteredProgram.DoesNotExist:
#         raise Http404("Registered Program does not exist")
#     return render(request, 'torontoevents/registered_program_detail.html', {'registered_program': registered_program})

class DropInProgramsListView(ListView):
    model = DropInProgram
    context_object_name = "dropin_programs"
    template_name = 'torontoevents/dropin_program_data_list.html'
  
def get_all_tuesday_classes(request):
    classes = RegisteredProgram.objects.filter(days_of_the_week='Tu')
    return render(request, 'torontoevents/registered_program_data_list.html', {'registered_programs': classes})
