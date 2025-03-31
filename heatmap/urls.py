from django.urls import path
from .views import home, stats, add, assaltos, dados_ano

urlpatterns = [
    path('', home, name = "home"),
    path('add/', add, name = "add" ),
    path('stats/', stats, name = 'stats'),
    path('assaltos/', assaltos, name = 'assaltos'),
    path('dados/<int:year>/', dados_ano, name = 'dados_ano' ), 
]
