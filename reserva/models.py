from django.db import models
from django.core.validators import RegexValidator

class Reserva(models.Model):
    TAMANHO_OPCOES = [
        ('pequeno', 'Pequeno'),
        ('medio', 'Médio'),
        ('grande', 'Grande'),
    ]

    HORARIO_OPCOES = [
        ('08:00', '08:00'),
        ('09:00', '09:00'),
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
    ]

    nomeDoPet = models.CharField(max_length=50, verbose_name='Nome do PET')
    raca = models.CharField(max_length=40, verbose_name='Raça')
    tamanho = models.IntegerField(verbose_name='Porte', choices=TAMANHO_OPCOES)
    nomeDoTutor = models.CharField(max_length=80, verbose_name='Nome do TUTOR')
    telefone = models.CharField(max_length=11, verbose_name='Telefone')
    email = models.EmailField(verbose_name='E-mail')
    data = models.DateField(verbose_name='Data')
    horario = models.CharField(max_length=5, choices=HORARIO_OPCOES)
    observacoes = models.TextField(verbose_name='Observações')
    
    class Meta:
        verbose_name = 'Reserva de Banho'
        verbose_name_plural = 'Reservas de Banho'