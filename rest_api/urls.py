from django.urls import path

from rest_api.views import adicionar_categoria, verificar_categorias

app_name = 'rest_api'

urlpatterns = [
    path('adicionar/', adicionar_categoria, name='categorias'),
    path('verificar/', verificar_categorias, name='verificar'),
]