from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {'listings': listings}
#   return HttpResponse("<h1>Hello World</h1>") # test the content shown correctly
    return render(request, 'pages/index.html', context) #goto templates/pages/ directory to find index.html

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context) #goto templates/pages/ directory to find about.html
