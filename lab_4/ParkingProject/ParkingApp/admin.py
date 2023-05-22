from django.contrib import admin
from .models import Auto, Check, ParkingPlace, Client

admin.site.register(Check)
admin.site.register(Client)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'brand', 'model']
    search_fields = ['^brand', '^model']


@admin.register(ParkingPlace)
class AutoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'price', 'isEmpty', 'auto']
    list_filter = ['price']
