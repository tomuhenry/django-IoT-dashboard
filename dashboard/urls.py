from django.urls import path
# from django.views.decorators.cache import cache_page

from . import views

app_name = 'dashboard'

urlpatterns = [
    path("light/", views.dashboard_light, name="light-data"),
    path("temperature/", views.dashboard_temp, name="temp-data"),
]
