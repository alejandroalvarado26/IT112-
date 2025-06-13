from django.shortcuts import render
from .models import Bands

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
