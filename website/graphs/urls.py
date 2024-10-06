from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="homePage"),
    path("stellarHosts", views.stellarHost, name="stellarHosts"),
    path("exoplants", views.exoplants, name="exoplants"),
    path("discoveryInfo", views.discoveryInfo, name="discoveryInfo")
]