from django.shortcuts import render, redirect
from django.urls import reverse

from captacao.forms import CandidatoForm
from captacao.models import Candidato, Periodo, Status, Marketing, Polo


def captacao(request):
    candidatos = Candidato.objects.all()

    context = {
        'candidatos': candidatos,
        'periodos': Periodo.objects.all(),
        'polos': Polo.objects.all(),
        'marketing_list': Marketing.objects.all(),
        'status_list': Status.objects.all(),
        'form': CandidatoForm(request.POST or None)
    }
    return render(request, 'captacao.html', context)


def modal_cria_candidato(request):
    form = CandidatoForm(request.POST or None)
    if form.is_valid():
        form.instance.atendente = request.user
        form.save()
        return redirect(reverse('captacao'))
    return render(request, 'modal_cria_candidato.html', {'form': form})
