from os import name
from django.urls import path
from .views import PaginaInicial


urlpatterns = [
    # Criar todos os endereços/rotas
    # path('endereço/', MinhaView.as_view(), name='referência/apelido'),
    path('inicio/', PaginaInicial.as_view(), name='index'),
    
]