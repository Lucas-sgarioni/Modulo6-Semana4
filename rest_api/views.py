from django.shortcuts import render

import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from base.models import Contato
from reserva.models import Reserva

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

@api_view(['GET'])
def verificar_reserva(request):
    consulta = Reserva.objects.all()
    dados = []
    for itens in consulta:
        dado = {
            'Informações do dono:':{
            'nome': itens.nomeDoTutor,
            'email': itens.email,
            'telefone': itens.telefone,
            },

            'Informações do PET':{
                'nome': itens.nomeDoPet,
                'raça': itens.raca,
                'tamanho': itens.tamanho,
            },
            
            'Informações sobre a reserva:':{
                'data': itens.data,
                'hora': itens.horario,
            },
            'observacao': itens.observacoes,
        }
        dados.append(dado)
    return Response(dados)