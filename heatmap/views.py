from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Robbery
from datetime import datetime
from .geocode.geocode import geocode_address
from django.contrib import messages
from .forms import RobberyForm


def is_staff(user):
    return user.is_authenticated and user.is_staff

def home(request):
    return render(request, "heatmap/home.html", {'show_year_dropdown': True})

def stats(request):
    return render(request, "heatmap/stats.html")

def add(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Você precisa estar logado para adicionar dados.')
        return redirect('login')
    
    elif request.method == "POST":
        form = RobberyForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            street = form.cleaned_data['street']
            number = form.cleaned_data['number']
            neighborhood = form.cleaned_data['neighborhood']
            description = form.cleaned_data['description']

            location = f"{street}, {number} - {neighborhood.name}"
            latitude, longitude = geocode_address(location)

            robbery = Robbery(
                date=date,
                time=time,
                street=street,
                number=number,
                neighborhood=neighborhood,
                description=description,
                latitude=latitude,
                longitude=longitude,
                is_valid=False,  
            )
            robbery.save()
            messages.success(request, 'Dados adicionados com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Erro ao adicionar dados. Verifique o formulário.')
            return render(request, "heatmap/add.html", {'form': form})
        
    elif request.method == "GET":
        form = RobberyForm(request.POST)
        return render(request, "heatmap/add.html", {'form': form})

def data_by_year(request, year):
    robberies_list = Robbery.objects.filter(date__year=year)
    data = []
    for robbery in robberies_list:
        location = f"{robbery.street}, {robbery.number} - {robbery.neighborhood.name}"
        data.append({
            'id': robbery.id,
            'Latitude': str(robbery.latitude),
            'Longitude': str(robbery.longitude),
            'Data': robbery.date.strftime('%d/%m/%Y'),
            'Hora': robbery.time.strftime('%H:%M'),
            'Descricao': robbery.description,
            'localizacao': location,
        })
    return JsonResponse(data, safe=False)
