from django.urls import path
from .views import home, stats, add

urlpatterns = [
    path('', home, name = "home"),
    path('add/', add, name = "add" ),
    path('stats/', stats, name = 'stats'),
]
