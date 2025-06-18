from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("bandslist/", views.bandsList, name="bands"),
    path("banddetail/<int:id>/", views.bandDetail, name="banddetail" ),
    path("bandslistJSON/", views.BandsListView.as_view(), name="bandslistJSON" ),
    path("bandscreateJSON/", views.BandsCreateView.as_view(), name="bandscreateJSON" ),
    path("bandsretrieveJSON/<int:id>", views.BandsRetrieveView.as_view(), name="bandsretrieveJSON")
]