from django.shortcuts import render

import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Contato

@api_view(['POST'])
def adicionar_categoria(request):
    nome = request.data['nome']
    email = request.data['email']
    mensagem = request.data['mensagem']
    contato = Contato.objects.create(
        nome = nome,
        email = email,
        mensagem = mensagem
    )
    dado = {
        'id': contato.id,
        'nome': contato.nome,
        'email': contato.email,
        'mensagem': contato.mensagem,
    }

    return Response(dado)

@api_view(['GET'])
def verificar_categorias(request):
    consulta = Contato.objects.all()
    dados = []
    for categoria in consulta:
        dado = {
            'id': categoria.id,
            'nome': categoria.nome,
            'e-mail': categoria.email,
            'mensagem': categoria.mensagem,
            'data': categoria.data,
        }
        dados.append(dado)
    return Response(dados)