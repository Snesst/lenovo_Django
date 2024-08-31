from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
#   return HttpResponse("<h1>Hello World</h1>") # test the content shown correctly
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html') #goto template directory to find pages
