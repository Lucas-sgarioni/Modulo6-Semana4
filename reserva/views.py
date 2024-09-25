from django.shortcuts import render
from reserva.forms import ReservaForm


def reserva(request):
    sucesso = False
    form = ReservaForm(request.POST or None)
    if form.is_valid():
        sucesso = True
        form.save()

    context = {
        'formulario': form,
        'sucesso': sucesso,
    }

    return render(request, 'reserva.html', context)

