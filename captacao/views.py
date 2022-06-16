import unicodedata

from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from captacao.forms import CandidatoForm, CreateNewForm, InscritoForm, ExAlunoForm
from captacao.models import Candidato, Periodo, Status, Marketing, Polo, Inscrito, ExAluno, Curso, Atendente, \
    SituacaoInscrito, SituacaoExAluno, Motivo


def login(request):
    return render(request, 'login_semantic.html')


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


def inscritos(request):
    inscritos = Inscrito.objects.filter(ativo=True)
    context = {
        'inscritos': inscritos,
        'form': InscritoForm(request.POST or None)
    }
    return render(request, 'inscritos.html', context)


def modal_cria_inscrito(request):
    print(request)
    form = InscritoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('inscritos'))
    return render(request, 'modal_cria_inscrito.html', {'form': form})


def modal_atualiza_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    form = InscritoForm(request.POST or None, instance=inscrito)
    if form.is_valid():
        inscrito.save()
        return redirect(reverse('inscritos'))
    return render(request, 'modal_atualiza_inscrito.html', {'form': form})


def modal_remove_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    if request.POST:
        inscrito.ativo = False
        inscrito.save()
        return redirect(reverse('inscritos'))
    else:
        return render(request, 'modal_remove_inscrito.html', {'inscrito': inscrito})


def exalunos(request):
    exalunos = ExAluno.objects.filter(ativo=True)

    context = {
        'exalunos': exalunos,
        'form': ExAlunoForm(request.POST or None)
    }
    return render(request, 'exalunos.html', context)

def modal_cria_exaluno(request):
    form = ExAlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('exalunos'))
    return render(request, 'modal_cria_exaluno.html', {'form': form})


def modal_atualiza_exaluno(request, pk):
    exaluno = get_object_or_404(ExAluno, pk=pk)
    form = ExAlunoForm(request.POST or None, instance=exaluno)
    if form.is_valid():
        exaluno.save()
        return redirect(reverse('exalunos'))
    return render(request, 'modal_atualiza_exaluno.html', {'form': form})


def modal_remove_exaluno(request, pk):
    exaluno = get_object_or_404(ExAluno, pk=pk)
    if request.POST:
        exaluno.ativo = False
        exaluno.save()
        return redirect(reverse('exalunos'))
    else:
        return render(request, 'modal_remove_exaluno.html', {'exaluno': exaluno})


# def alunos(request):
#     alunos = Aluno.objects.filter(ativo=True)
#
#     context = {
#         'alunos': alunos,
#         'form': AlunoForm(request.POST or None)
#     }
#     return render(request, 'alunos.html', context)
#
# def modal_cria_aluno(request):
#     form = AlunoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('alunos'))
#     return render(request, 'modal_cria_aluno.html', {'form': form})
#
#
# def modal_atualiza_aluno(request, pk):
#     aluno = get_object_or_404(Aluno, pk=pk)
#     form = AlunoForm(request.POST or None, instance=aluno)
#     if form.is_valid():
#         aluno.save()
#         return redirect(reverse('alunos'))
#     return render(request, 'modal_atualiza_aluno.html', {'form': form})
#
#
# def modal_remove_aluno(request, pk):
#     aluno = get_object_or_404(Aluno, pk=pk)
#     if request.POST:
#         aluno.ativo = False
#         aluno.save()
#         return redirect(reverse('alunos'))
#     else:
#         return render(request, 'modal_remove_aluno.html', {'aluno': aluno})


class CreateNewName(View):
    def get(self, request):
        dic_tables = {
            'Período': Periodo,
            'Polo': Polo,
            'Curso': Curso,
            'Marketing': Marketing,
            'Atendente': Atendente,
            'Status': Status,
            'Situação do inscrito': SituacaoInscrito,
            'Situação do ex-aluno': SituacaoExAluno,
            'Motivo': Motivo
        }
        nome = request.GET.get('novo_nome', None)
        h4_text = request.GET.get('h4_text', None)
        obj = dic_tables[h4_text].objects.create(nome=nome)
        select_id = unicodedata.normalize("NFD", h4_text.lower().split()[0]).encode("ascii", "ignore").decode("utf-8")
        novo = {'id': obj.id, 'nome': obj.nome, 'h4_text': h4_text, 'select_id': f'#id_{select_id}'}
        data = {'novo': novo}
        return JsonResponse(data)


def periodos(request):
    periodos = Periodo.objects.filter(ativo=True)
    context = {
        'periodos': periodos
    }
    return render(request, 'periodos.html', context)
