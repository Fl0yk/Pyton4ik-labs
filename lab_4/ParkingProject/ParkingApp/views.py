from audioop import reverse
from cmath import log
import requests
import random
import logging
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from plotly.graph_objects import Bar, Layout, Figure
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.views import generic, View
from datetime import date, datetime
from .models import Auto, ParkingPlace, Client, Check


logger = logging.getLogger(__name__)

def index(request):
    now = datetime.now()
    url = 'https://official-joke-api.appspot.com/random_joke'
    try:
        res = requests.get(url).json()

        joke_setup = res['setup']
        joke_punch = res['punchline']
    except:
        joke_setup = 'There will be no joke('
        joke_punch = ''

    num_empty_placces=ParkingPlace.objects.filter(isEmpty__exact=True).count()

    return render(
        request,
        "ParkingApp/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        {
            'content' : now.strftime("%d/%m/%y"),
            'num_empty_placces' : num_empty_placces,
            'setup' : joke_setup,
            'punch' : joke_punch
        } 
    )

def about(request):
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(random.randint(1, 1010))
    res = requests.get(url).json()

    pokemon_name = res['name']
    pokemon_image = res['sprites']['front_default']
    return render(
        request,
        "ParkingApp/about.html",
        {
            'title' : "Bobik",
            'name' : pokemon_name,
            'image' : pokemon_image
        }
    )

class EmptyPlacesView(generic.ListView):
    model = ParkingPlace
    template_name = 'ParkingApp/empty_place_list.html'

    def get_queryset(self):
        return ParkingPlace.objects.filter(isEmpty__exact=True)

@method_decorator(login_required, name='dispatch')
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


def validate_name(value):
    if Client.objects.filter(name=value).exists():
        raise forms.ValidationError('Name is already taken', params={'value' : value})

def validate_mail(value):
    if User.objects.filter(email=value).exists():
        raise forms.ValidationError('Email is already taken', params={'value' : value})

class ClientForm(forms.Form):
    num_validetor = RegexValidator(regex=r"^\+375 \(29\) \d{3}-\d{2}-\d{2}$")

    name = forms.CharField(max_length=20, min_length=2, validators=[validate_name])
    mail = forms.EmailField(max_length=30, min_length=5, validators=[validate_mail])
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
            logger.info(f'Registration new user {client.id}: {client.name}')
            return HttpResponseRedirect('/accounts/login/')
        else:
            logger.error('Failed to registration user')
    else:
        clientForm = ClientForm()

    return render(
            request,
            'ParkingApp/registration.html',
            context={'form' : clientForm, })

class CarForm(forms.Form):
    model = forms.CharField(max_length=20, min_length=2)
    brand = forms.CharField(max_length=20, min_length=2)

@login_required
def createAuto(request):
    client = Client.objects.get(username=request.user.username)

    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = Auto()
            car.model = form.cleaned_data['model']
            car.brand = form.cleaned_data['brand']
            if Auto.objects.filter(model=car.model, brand=car.brand).exists():
                return render(request, 
                          'ParkingApp/user_cars.html', 
                          {'object_list' : client.cars.all(), 'form' : form}
                          )
            car.save()
            client.cars.add(car)
            logger.info(f'User {client.name} create new car')
        else:
            logger.error(f'Failed to create new car by {client.name}')
    else:
        form = CarForm()

    return render(request, 
                  'ParkingApp/user_cars.html', 
                  {'object_list' : client.cars.all(), 'form' : form}
                 )

@login_required
def editAuto(request, id):
    try:
        car = Auto.objects.get(id=id)
        if request.method == 'POST':
            car.model = request.POST.get('model')
            car.brand = request.POST.get('brand')
            car.save()
            logger.info(f'Edit car by {request.user.username}')
            return HttpResponseRedirect('/personal/cars')
        else:
            return render(request, 'ParkingApp/edit_auto.html', {'car' : car})

    except Auto.DoesNotExist:
        logger.info(f'Auto does not exist by {request.user.username}')
        raise Http404('Auto not found')

@login_required
def deleteAuto(request, id):
    try:
        car = Auto.objects.get(id=id)
        if ParkingPlace.objects.filter(auto=car).exists():
            place = ParkingPlace.objects.filter(auto=car).get()
            place.isEmpty = True
            place.save()
        car.delete()
        logger.info(f'Delete auto by {request.user.username}')
        return HttpResponseRedirect('/personal/cars')
    except Auto.DoesNotExist:
        logger.info(f'Auto does not exist by {request.user.username}')
        raise Http404('Auto not found')

@method_decorator(login_required, name='dispatch')
class UserPlacesView(generic.ListView):
    model = ParkingPlace
    template_name = 'ParkingApp/user_places.html'

    def get_queryset(self):
        client = Client.objects.get(username=self.request.user.username)
        return ParkingPlace.objects.filter(auto__in=client.cars.all())

@method_decorator(login_required, name='dispatch')
class UserChecksView(generic.ListView):
    model = Auto
    template_name = 'ParkingApp/user_checks.html'

    def get_queryset(self):
        client = Client.objects.get(username=self.request.user.username)
        return client.check_set.all()

def validate_place(value):
    if not ParkingPlace.objects.filter(id=value, isEmpty=True).exists():
        raise forms.ValidationError('Place not found', params={'value' : value})

def validate_car(value):
    if not Auto.objects.filter(id=value, parkingplace__exact=None).exists():
        raise forms.ValidationError('Car not found', params={'value' : value})


class TakePlaceForm(forms.Form):
    carId = forms.IntegerField(max_value=999, min_value=1, validators=[validate_car])
    placeId = forms.IntegerField(max_value=999, min_value=1, validators=[validate_place])


@login_required
def TakePlace(request):
    if request.method == "POST":
        form = TakePlaceForm(request.POST)
        if form.is_valid():
            car = Auto.objects.filter(id=form.cleaned_data['carId']).get()
            place = ParkingPlace.objects.filter(id=form.cleaned_data['placeId']).get()
            place.auto = car
            place.isEmpty = False
            place.save()
            logger.info(f'User {request.user.username} take a place')
        else:
            logger.error(f'Failed take a place by {request.user.username}')
    else:
        form = TakePlaceForm()

    empty_place = ParkingPlace.objects.filter(isEmpty__exact=True)
    return render(
            request,
            'ParkingApp/take_place.html',
            context={'form' : form,
                     'places' : empty_place })


@login_required
def AdminStatistics(request):
    if not request.user.is_superuser:
        raise Http404('You are not admin')

    if request.method == 'POST':
        now = datetime.now().date()
        for place in ParkingPlace.objects.filter(isEmpty__exact=False):
            car = place.auto
            owners = car.client_set.all() #Client.objects.filter(cars__contains=car)
            check = Check()
            check.place = place
            check.save()

            for owner in owners:
                lastCheck = owner.check_set.filter(place=place).last()
                if lastCheck and lastCheck.dateOfActual.year == now.year and lastCheck.dateOfActual.month == now.month:
                    continue
                owner.check_set.add(check)
                owner.balance -= place.price
                owner.save()
    
    months = []
    profits = []

    for m in range(1, 13):
        months.append(m)
        checks_of_month = Check.objects.filter(dateOfActual__month=m)
        sum = 0
        for check in checks_of_month:
            sum += check.place.price
        profits.append(sum)

    data = Bar(x=months, y=profits)
    layoyt = Layout(title='Parking profit',
                    xaxis=dict(title='Months'),
                    yaxis=dict(title='profits'))
    fig = Figure(data=data, layout=layoyt)

    return render(
        request,
        'ParkingApp/admin_statistic.html',
        context={'plot' : fig.to_html(full_html=False), }
        )



class BalanceForm(forms.Form):
    money = forms.DecimalField(min_value=0, max_digits=6, decimal_places=2)

@login_required
def UpBalance(request):
    if request.method == "POST":
        form = BalanceForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(username=request.user.username)
            client.balance += form.cleaned_data['money']
            client.save()
            logger.info(f'User {client.name} replenished the balance')
            return HttpResponseRedirect('/personal/')
    else:
        form = BalanceForm()

    return render(
            request,
            'ParkingApp/up_balance.html',
            context={'form' : form })
    

