from audioop import reverse
from msilib.schema import CreateFolder
from urllib import response
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
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

class ClientForm(forms.Form):
    num_validetor = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")

    name = forms.CharField(max_length=20)
    mail = forms.EmailField()
    number = forms.CharField(max_length=20, validators=[num_validetor], help_text="+375 (29) xxx-xx-xx")
    password = forms.CharField(widget=forms.PasswordInput())



def UserRegistration(request):
    if request.method == "POST":
        clientForm = ClientForm(request.POST)
        if clientForm.is_valid():
            user = User()
            user.username = clientForm.cleaned_data['name']
            user.email = clientForm.cleaned_data['mail']
            user.password = make_password(clientForm.cleaned_data['password'])
            user.save()
            request.user = user
            client = Client()
            client.name = user.username
            client.username = user.username
            client.number = clientForm.cleaned_data['number']
            client.balance = 0
            client.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        clientForm = ClientForm()

    return render(
            request,
            'ParkingApp/registration.html',
            context={'form' : clientForm, })


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



