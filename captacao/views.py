import unicodedata

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from captacao.forms import CandidatoForm, InscritoForm, AlunoForm, ExAlunoForm
from captacao.models import (
    Candidato, Periodo, Status, Marketing, Polo, Inscrito, Curso,
    SituacaoInscrito, SituacaoExAluno, Motivo, Aluno, ExAluno, AtendimentosAluno
)

@login_required
def home(request):
    return render(request, 'home.html')


@login_required
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
        form.instance.criado_por = request.user
        form.save()
        return redirect(reverse('candidatos'))
    return render(request, 'modal_cria_candidato.html', {'form': form})


def modal_atualiza_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    # atendimentos = candidato.atendimentos_aluno.all()
    form = CandidatoForm(request.POST or None, instance=candidato)
    if form.is_valid():
        candidato.atualizado_por = request.user
        candidato.save()
        return redirect(reverse('candidatos'))
    return render(request, 'modal_atualiza_candidato.html', {'form': form, 'estudante': candidato})


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
    return render(request, 'modal_atualiza_inscrito.html', {'form': form, 'estudante': inscrito})


def modal_remove_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    if request.POST:
        inscrito.ativo = False
        inscrito.save()
        return redirect(reverse('inscritos'))
    else:
        return render(request, 'modal_remove_inscrito.html', {'inscrito': inscrito})


def exalunos(request):
    periodo = None
    filtro = request.POST.get('select-periodo')
    if filtro and not filtro == '0':
        periodo = Periodo.objects.get(pk=int(filtro))
        exalunos = ExAluno.objects.filter(periodos=periodo, ativo=True)
    else:
        exalunos = ExAluno.objects.filter(ativo=True)

    context = {
        'exalunos': exalunos,
        'form': ExAlunoForm(request.POST or None),
        'periodos': Periodo.objects.all(),
        'filtro': periodo
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
    return render(request, 'modal_atualiza_exaluno.html', {'form': form, 'estudante': exaluno})


def modal_remove_exaluno(request, pk):
    exaluno = get_object_or_404(ExAluno, pk=pk)
    if request.POST:
        exaluno.ativo = False
        exaluno.save()
        return redirect(reverse('exalunos'))
    else:
        return render(request, 'modal_remove_exaluno.html', {'exaluno': exaluno})


def alunos(request):
    periodo = None
    filtro = request.POST.get('select-periodo')
    if filtro and not filtro == '0':
        periodo = Periodo.objects.get(pk=int(filtro))
        alunos = Aluno.objects.filter(periodos=periodo, ativo=True)
    else:
        alunos = Aluno.objects.filter(ativo=True)

    context = {
        'alunos': alunos,
        'form': AlunoForm(request.POST or None),
        'periodos': Periodo.objects.all(),
        'filtro': periodo
    }
    return render(request, 'alunos.html', context)


def modal_cria_aluno(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('alunos'))
    return render(request, 'modal_cria_aluno.html', {'form': form})


def modal_atualiza_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        aluno.save()
        return redirect(reverse('alunos'))
    return render(request, 'modal_atualiza_aluno.html', {'form': form, 'estudante': aluno})


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


class CreateNewAttendance(View):
    def get(self, request):
        months = {
            1: 'Janeiro',
            2: 'Fevereiro',
            3: 'Março',
            4: 'Abril',
            5: 'Maio',
            6: 'Junho',
            7: 'Julho',
            8: 'Agosto',
            9: 'Setembro',
            10: 'Outubro',
            11: 'Novembro',
            12: 'Dezembro'
        }
        descricao = request.GET.get('descricao', None)
        candidato_id = request.GET.get('candidato', None)
        if descricao and candidato_id:
            candidato = Candidato.objects.get(pk=int(candidato_id))
            obj = AtendimentosAluno.objects.create(descricao=descricao, candidato=candidato)
            obj_data = f'{obj.data.day} de {months[obj.data.month]} de {obj.data.year} às {obj.data.time().strftime("%H:%M")}'
            data = {'data': obj_data, 'descricao': obj.descricao}
            return JsonResponse(data)
        return JsonResponse({})

def periodos(request):
    periodos = Periodo.objects.filter(ativo=True)
    context = {
        'periodos': periodos
    }
    return render(request, 'periodos.html', context)
