from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from datetime import datetime
from .models import Auto, ParkingPlace, Client, Check

def index(request):
    now = datetime.now()

    num_empty_placces=ParkingPlace.objects.filter(isEmpty__exact=True).count()

    return render(
        request,
        "ParkingApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content' : now.strftime("%d/%m/%y"),
            'num_empty_placces' : num_empty_placces
        } 
    )

def about(request):
    return render(
        request,
        "ParkingApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )

class EmptyPlacesView(generic.ListView):
    model = ParkingPlace
    template_name = 'ParkingApp/empty_place_list.html'

    def get_queryset(self):
        return ParkingPlace.objects.filter(isEmpty__exact=True)
