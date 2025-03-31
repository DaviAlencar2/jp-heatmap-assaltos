from django.shortcuts import render

def home(request):
    return render(request, "heatmap/home.html", {'show_year_dropdown': True})

def stats(request):
    return render(request, "heatmap/stats.html")

def add(request):
    return render(request, "heatmap/add.html")
