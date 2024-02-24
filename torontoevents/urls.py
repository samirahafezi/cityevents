from django.urls import path

from . import views

urlpatterns = [
    path('torontoevents/', views.HomeView.as_view()),
    path('authorized', views.AuthorizedView.as_view()),
    path('locations/',views.LocationsListView.as_view()),
    path('facilities/',views.FacilitiesListView.as_view()),
    path('registeredprograms/',views.RegisteredProgramsListView.as_view(), name="registeredprograms.list"),
    path('registeredprograms/<int:pk>',views.RegisteredProgramDetailView.as_view(), name="registeredprograms.detail"),
    path('dropinprograms/',views.DropInProgramsListView.as_view()),
]
