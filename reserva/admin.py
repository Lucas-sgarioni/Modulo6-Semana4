from django.contrib import admin
from reserva.models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nomeDoTutor', 'email','telefone', 'nomeDoPet', 'data', 'horario']
    search_fields = ['nomeDoTutor', 'email', 'nomeDoPet']
    list_filter = ['data', 'horario', 'tamanho']

