from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from captacao.forms import CandidatoForm, PeriodoForm
from captacao.models import Candidato, Periodo, Status, Marketing, Polo, Inscrito, ExAluno


def captacao(request):
    return render(request, 'base.html')


def candidatos(request):
    candidatos = Candidato.objects.all()
    context = {
        'candidatos': candidatos,
        'periodos': Periodo.objects.all(),
        'polos': Polo.objects.all(),
        'marketing_list': Marketing.objects.all(),
        'status_list': Status.objects.all(),
        'form': CandidatoForm(request.POST or None),
    }
    return render(request, 'candidatos.html', context)


def inscritos(request):
    inscritos = Inscrito.objects.all()

    context = {
        'inscritos': inscritos,
        'periodos': Periodo.objects.all(),
        'polos': Polo.objects.all(),
        'status_list': Status.objects.all(),
        # 'form': InscritoForm(request.POST or None)
    }
    return render(request, 'inscritos.html', context)


def exalunos(request):
    ex_alunos = ExAluno.objects.all()

    context = {
        'ex_alunos': ex_alunos,
        'periodos': Periodo.objects.all(),
        'polos': Polo.objects.all(),
        'status_list': Status.objects.all(),
        # 'form': ExAlunoForm(request.POST or None)
    }
    return render(request, 'ex-alunos.html', context)


def modal_cria_candidato(request):
    form = CandidatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('candidatos'))
    return render(request, 'modal_cria_candidato.html', {'form': form})


def modal_atualiza_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    form = CandidatoForm(request.POST or None, instance=candidato)
    if form.is_valid():
        candidato.save()
        return redirect(reverse('candidatos'))
    return render(request, 'modal_atualiza_candidato.html', {'form': form})


def modal_remove_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.POST:
        candidato.delete()
        return redirect(reverse('candidatos'))
    else:
        return render(request, 'modal_remove_candidato.html', {'candidato': candidato})


class CreateCrudPeriodo(View):
    def get(self, request):
        nome = request.GET.get('novo_nome', None)

        obj = Periodo.objects.create(nome=nome)

        periodo = {'id': obj.id, 'nome': obj.nome}

        data = {'periodo': periodo}
        return JsonResponse(data)


def periodos(request):
    periodos = Periodo.objects.all()
    context = {
        'periodos': periodos
    }
    return render(request, 'periodos.html', context)
