from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'myapp/home.html')

def busmap(request):
    return render(request, 'myapp/busmap.html')

def login(request):
    return render(request, 'myapp/login.html')

def map_view(request):
    return render(request, 'myapp/map_view.html')

def info(request):
    return render(request, 'myapp/info.html')