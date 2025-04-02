from django.shortcuts import render
from django.http import JsonResponse
from .models import Robbery
from datetime import datetime
from .geocode.geocode import geocode_address

def home(request):
    return render(request, "heatmap/home.html", {'show_year_dropdown': True})

def stats(request):
    return render(request, "heatmap/stats.html")

def add(request):
    return render(request, "heatmap/add.html")

# Eu sei que essa implementacao é ruim, irei melhorar com formulario e autorizaçao

def data_by_year(request, year):
    robberies_list = Robbery.objects.filter(date__year=year)
    data = []
    for robbery in robberies_list:
        if robbery.location.latitude == "" or robbery.location.longitude == "":
            location = f"{robbery.location.street}, {robbery.location.number} - {robbery.location.neighborhood.name}"
        latitude, longitude = geocode_address(location)
        data.append({
            'id': robbery.id,
            'Latitude': str(latitude),
            'Longitude': str(longitude),
            'Data': robbery.date.strftime('%d/%m/%Y'),
            'Hora': robbery.time.strftime('%H:%M'),
            'Descricao': robbery.description,
            'localizacao': location,
        })
    return JsonResponse(data, safe=False)
