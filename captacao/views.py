import unicodedata

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from captacao.forms import CandidatoForm, CreateNewForm
from captacao.models import Candidato, Periodo, Status, Marketing, Polo, Inscrito, ExAluno


def captacao(request):
    return render(request, 'base.html')


def candidatos(request):
    candidatos = Candidato.objects.filter(ativo=True)
    context = {
        'candidatos': candidatos,
        'form': CandidatoForm(request.POST or None),
        # 'form_create_new': CreateNewForm()
    }
    return render(request, 'candidatos.html', context)


def inscritos(request):
    inscritos = Inscrito.objects.filter(ativo=True)

    context = {
        'inscritos': inscritos,
        # 'form': InscritoForm(request.POST or None)
    }
    return render(request, 'inscritos.html', context)


def exalunos(request):
    ex_alunos = ExAluno.objects.filter(ativo=True)

    context = {
        'ex_alunos': ex_alunos,
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
        candidato.ativo = False
        candidato.save()
        return redirect(reverse('candidatos'))
    else:
        return render(request, 'modal_remove_candidato.html', {'candidato': candidato})


class CreateNewName(View):
    def get(self, request):
        dic_tables = {
            'Período': Periodo,
            'Polo': Polo,
        }
        nome = request.GET.get('novo_nome', None)
        h4_text = request.GET.get('h4_text', None)
        obj = dic_tables[h4_text].objects.create(nome=nome)
        select_id = unicodedata.normalize("NFD", h4_text.lower()).encode("ascii", "ignore").decode("utf-8")
        novo = {'id': obj.id, 'nome': obj.nome, 'h4_text': h4_text, 'select_id': f'#id_{select_id}'}
        data = {'novo': novo}
        return JsonResponse(data)


def periodos(request):
    periodos = Periodo.objects.filter(ativo=True)
    context = {
        'periodos': periodos
    }
    return render(request, 'periodos.html', context)
