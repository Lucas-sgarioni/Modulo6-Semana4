from datetime import date
from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nomeDoPet', 'raca', 'tamanho', 'nomeDoTutor', 'telefone', 'email', 'data', 'horario', 'observacoes']
        widgets = {
            'data': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date', 'min': date.today()}),
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'data' in self.data:
                data_selecionada = self.data.get('data')
                reservas_existentes = Reserva.objects.filter(data=data_selecionada)
                horarios_reservados = reservas_existentes.values_list('horario', flat=True)
                horarios_disponiveis = [choice for choice in Reserva.HORARIO_CHOICES if choice[0] not in horarios_reservados]
                self.fields['horario'].choices = horarios_disponiveis