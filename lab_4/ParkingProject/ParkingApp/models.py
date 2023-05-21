import re
import uuid
from wsgiref.validate import validator
from django.db import models
from django.core.validators import RegexValidator


class ParkingPlace(models.Model):
    num = models.UUIDField(primary_key=True, default=uuid.uuid4)
    isEmpty = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    auto = models.OneToOneField('Auto', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Parking place"
        verbose_name_plural = "Parking places"

    def __str__(self) -> str:
        return self.num


class Check(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    dateOfActual = models.DateField(auto_now_add=True)
    place = models.ForeignKey(ParkingPlace, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Check"
        verbose_name_plural = "Checks"

    def __str__(self) -> str:
        return str(self.id) + "\nDate: " + str(self.dateOfActual) + "\nPlace: " + str(self.place)


class Auto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self) -> str:
        return self.brand + "\n" + self.model


class Client(models.Model):
    num_validetor = RegexValidator(regex=r"^+375 \(29\) \d{3}-\d{2}-\d{2}$")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=20)
    number = models.CharField(max_length=20, validators=[num_validetor], default='+375 (29) xxx-xx-xx')
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    cars = models.ManyToManyField(Auto)
    checks = models.ForeignKey(Check, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return self.name + "\n" + self.number



