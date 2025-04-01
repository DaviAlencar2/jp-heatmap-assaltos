from django.contrib import admin
from .models import Assalto

class ListarAssaltos(admin.ModelAdmin):
    list_display = ("id","location","date","time")
    list_display_links = ("id","location")
    search_fields = ("date","location")
    list_filter = ("type",)
    list_per_page = 10

admin.site.register(Assalto,ListarAssaltos)