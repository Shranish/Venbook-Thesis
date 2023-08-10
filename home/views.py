
from django.shortcuts import render
from accounts.models import VenueAccount, is_verified

# Create your views here.
def index(request):
    return render(request,'home/index.html')


def search(request):
    query=request.GET['location']
    allPosts = is_verified.objects.filter(verified = True, venue_account__city__icontains=query)
    params={
        'allPosts': allPosts
        }   
    return render(request, 'venue/displaypage.html', params)