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
def assaltos(request):
    assaltos_list = Robbery.objects.all()
    data = []
    for assalto in assaltos_list:
        data.append({
            'id': assalto.id,
            'latitude': assalto.latitude,
            'longitude': assalto.longitude,
            'data': assalto.date.strftime('%d/%m/%Y'),
            'hora': assalto.time.strftime('%H:%M'),
            'descricao': assalto.description,
            'localizacao': assalto.location.neighborhood.name,
        })
    return JsonResponse(data, safe=False)

def dados_ano(request, year):
    assaltos_list = Robbery.objects.filter(date__year=year)
    data = []
    for assalto in assaltos_list:
        if assalto.location.latitude == "" or assalto.location.longitude == "":
            location = f"{assalto.location.street}, {assalto.location.number} - {assalto.location.neighborhood.name}"
        latitude, longitude = geocode_address(location)
        data.append({
            'id': assalto.id,
            'Latitude': str(latitude),
            'Longitude': str(longitude),
            'Data': assalto.date.strftime('%d/%m/%Y'),
            'Hora': assalto.time.strftime('%H:%M'),
            'Descricao': assalto.description,
            'localizacao': location,
        })
    return JsonResponse(data, safe=False)

