#from django.conf.urls import include, url
from django.urls import include, re_path, path
from django.contrib import admin
import ParkingApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^$', ParkingApp.views.index, name='index'),
    re_path(r'^home$', ParkingApp.views.index, name='home'),
    re_path(r'^about$', ParkingApp.views.about, name='about'),

    path('admin/', admin.site.urls)
]