from audioop import reverse
from msilib.schema import CreateFolder
from urllib import response
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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


class UserProfileView(View):
    @staticmethod
    def get(request):
        try:
            client = Client.objects.get(username=request.user.username)
        except Client.DoesNotExist:
            raise Http404('Client not found')

        return render(
            request,
            'ParkingApp/personal_page.html',
            context={'client' : client, })


class UserCarsView(generic.ListView):
    model = Auto
    template_name = 'ParkingApp/user_cars.html'

    def get_queryset(self):
        client = Client.objects.get(username=self.request.user.username)
        return client.cars.all()


def createAuto(request):
    if request.method == 'POST':
        client = Client.objects.get(username=request.user.username)
        car = Auto()
        car.model = request.POST.get('model')
        car.brand = request.POST.get('brand')
        car.save()
        client.cars.add(car)
    return HttpResponseRedirect('/personal/cars')

def editAuto(request, id):
    try:
        car = Auto.objects.get(id=id)
        if request.method == 'POST':
            car.model = request.POST.get('model')
            car.brand = request.POST.get('brand')
            car.save()
            return HttpResponseRedirect('/personal/cars')
        else:
            return render(request, 'ParkingApp/edit_auto.html', {'car' : car})

    except Auto.DoesNotExist:
        raise Http404('Auto not found')

def deleteAuto(request, id):
    try:
        car = Auto.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect('/personal/cars')
    except Auto.DoesNotExist:
        raise Http404('Auto not found')


class UserPlacesView(generic.ListView):
    model = ParkingPlace
    template_name = 'ParkingApp/user_places.html'

    def get_queryset(self):
        client = Client.objects.get(username=self.request.user.username)
        return ParkingPlace.objects.filter(auto__in=client.cars.all())



