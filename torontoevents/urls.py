from django.urls import path

from . import views

urlpatterns = [
    path('torontoevents/', views.home),
    path('authorized', views.authorized)
]
