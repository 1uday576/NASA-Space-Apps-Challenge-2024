from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homePage"),
    path("stellarHosts", views.stellarHost, name="stellarHosts"),
    path("exoplanets", views.exoplanets, name="exoplanets"),
    path("discoveryInfo", views.discoveryInfo, name="discoveryInfo")
]