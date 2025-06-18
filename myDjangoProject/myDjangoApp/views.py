from django.shortcuts import render
from .models import Bands
from .serializers import BandSerializer
from rest_framework import generics

def home(request):
    username =  request.GET.get('username', '')
    context = {"username" : username}
    return render(request, "myDjangoApp/home.html", context)

def bandsList(request):
    data = Bands.objects.all()
    context = {"bands" : data}
    return render(request, "myDjangoApp/bands.html", context)

def bandDetail(request, id):
    band = Bands.objects.get(id=id)
    return render(request, "myDjangoApp/banddetail.html", {"band" : band})

class BandsListView(generics.ListAPIView):
    queryset = Bands.objects.all()
    serializer_class = BandSerializer

class BandsRetrieveView(generics.RetrieveAPIView):
    queryset = Bands.objects.all()
    serializer_class = BandSerializer
    lookup_field = "id"

class BandsCreateView(generics.CreateAPIView):
    queryset = Bands.objects.all()
    serializer_class = BandSerializer

