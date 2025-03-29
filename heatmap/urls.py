from django.urls import path
from .views import home, stats, add

urlpatterns = [
    path('', home, name = "home"),
    path('adicionar_assalto/', add, name = "add" ),
    path('estatisticas/', stats, name = "stats"),
]
