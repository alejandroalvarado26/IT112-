from django.shortcuts import render

def home(request):
    username =  request.GET.get('username', '')
    context = {"username" : username}
    return render(request, "myDjangoApp/home.html", context)
