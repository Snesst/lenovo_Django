from django.shortcuts import render
from .models import Listing
# Create your views here.

def index(request):
    # get all data from listing database
    listings = Listing.objects.all()
    #pass database records into listings context
    context = {'listings':listings}
    return render(request, 'listings/listings.html',context) #goto templates/listings/ directory to find listings.html

def listing(request):
    return render(request, 'listings/listing.html') #goto templates/listings/ directory to find listing.html

def search(request):
    return render(request, 'listings/search.html') #goto templates/listings/ directory to find search.html
# Create your views here.
