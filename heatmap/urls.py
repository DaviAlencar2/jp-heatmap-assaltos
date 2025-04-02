from django.urls import path
from .views import home, stats, add, data_by_year

urlpatterns = [
    path('', home, name = "home"),
    path('add/', add, name = "add" ),
    path('stats/', stats, name = 'stats'),
    path('dados/<int:year>/', data_by_year, name = 'dados_ano' ), 
]
