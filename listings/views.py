from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

# Create your views here.

def index(request):
    # get all data from listing database
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    #pass database records into listings context
    context = {'listings':paged_listings}
    return render(request, 'listings/listings.html',context) #goto templates/listings/ directory to find listings.html

def listing(request, listing_id): #listing_id into this function, matching the variable from urls.py
    return render(request, 'listings/listing.html') #goto templates/listings/ directory to find listing.html

def search(request):
    return render(request, 'listings/search.html') #goto templates/listings/ directory to find search.html
# Create your views here.
