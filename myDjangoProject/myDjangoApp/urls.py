from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("bandslist", views.bandsList, name="bands"),
    path("banddetail/<int:id>/", views.bandDetail, name="banddetail" )
]