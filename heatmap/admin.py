from django.contrib import admin
from .models import Assalto

class ListarAssaltos(admin.ModelAdmin):
    list_display = ("id","location","date","time")
    list_display_links = ("id","location")
    search_fields = ("date","location")

admin.site.register(Assalto,ListarAssaltos)