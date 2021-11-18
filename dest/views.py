from django.shortcuts import render , redirect
from django.http import HttpResponse
from dest.models import Package , Hotel
# Create your views here.
def dest(request):
    allposts = Package.objects.all()
    context={
        'allposts':allposts
    }
    return render(request, "dest/package.html", context)

def hotels(request):
    hotels = Hotel.objects.all()
    allposts= Package.objects.all()
    con = {
        'hotels':hotels,
        'allposts':allposts
    }
    return render(request, "dest/hotels.html", con)
    if request.method=="POST":
        location=request.POST['location']
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        room=request.POST['room']
        adult=request.POST['adult']
        child=request.POST['child']
        print(location, checkin, checkout, room, adult, child)
        con={
            'location':location
        }
        if location is Null:
            return render(request, "dest/hotels.html", con)

def bookmark(request):
    return HttpResponse("bookmarks")

def detail(request,slug):
    post=Package.objects.filter(slug=slug).first()
    context = {
        'post':post
    }
    return render(request, "dest/detail.html", context)