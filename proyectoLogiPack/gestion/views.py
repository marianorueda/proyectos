from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'gestion/index.html')

def options(request):
    return render(request, 'gestion/options.html')