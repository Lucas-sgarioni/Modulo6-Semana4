from django.urls import path

from rest_api.views import adicionar_categoria, verificar_categorias, verificar_reserva

app_name = 'rest_api'

urlpatterns = [
    path('adicionar/', adicionar_categoria, name='categoria'),
    path('verificar/', verificar_categorias, name='verificar'),
    path('reserva/', verificar_reserva, name='reserva'),
]