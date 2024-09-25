from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    email = models.EmailField(verbose_name='E-mail')
    mensagem = models.TextField(verbose_name='Mensagem')
    data = models.DateTimeField(verbose_name='Enviado em', auto_now_add=True)
    lido = models.BooleanField(verbose_name='Lido', default=False, blank=True)

    class Meta:
        verbose_name = 'Formulário de Contato'
        verbose_name_plural = 'Formulários de Contatos'
        ordering = ['-data']
