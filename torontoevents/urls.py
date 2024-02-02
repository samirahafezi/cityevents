from django.urls import path

from . import views

urlpatterns = [
    path('torontoevents/', views.home),
    path('authorized', views.authorized),
    path('locations/',views.list_locations_data),
    path('facilities/',views.list_facilities_data),
    path('registeredprograms/',views.list_registered_programs_data),
]
