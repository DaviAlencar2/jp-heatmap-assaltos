from django.contrib import admin
from .models import Robbery, Location, Neighborhood

class ListarAssaltos(admin.ModelAdmin):
    list_display = ("id","location","date","time")
    list_display_links = ("id","location")
    search_fields = ("date","location")
    list_filter = ("type",)
    list_per_page = 10

admin.site.register(Robbery, ListarAssaltos)
admin.site.register(Location)
admin.site.register(Neighborhood)