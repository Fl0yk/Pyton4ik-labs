#from django.conf.urls import include, url
from django.urls import include, re_path, path
from django.contrib import admin
import ParkingApp.views

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    re_path(r'^$', ParkingApp.views.index, name='index'),
    re_path(r'^home$', ParkingApp.views.index, name='home'),
    re_path(r'^about$', ParkingApp.views.about, name='about'),
    re_path(r'^places$', ParkingApp.views.EmptyPlacesView.as_view(), name='places'),
    re_path(r'^personal/$', ParkingApp.views.UserProfileView.as_view(), name='user'),
    re_path(r'^personal/cars$', ParkingApp.views.UserCarsView.as_view(), name='user_cars'),
    re_path(r'^personal/createAuto/$', ParkingApp.views.createAuto, name='create_auto'),
    path('personal/editAuto/<int:id>/', ParkingApp.views.editAuto, name='edit_auto'),
    path('personal/deleteAuto/<int:id>/', ParkingApp.views.deleteAuto, name='delete_auto'),
    re_path(r'^personal/places$', ParkingApp.views.UserPlacesView.as_view(), name='user_places'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls)
]