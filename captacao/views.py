import unicodedata

from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View

from captacao.forms import CandidatoForm, InscritoForm, AlunoForm, ExAlunoForm, AtendimentosCandidatoForm
from captacao.models import (
    Candidato, Periodo, Inscrito, Aluno, ExAluno, AtendimentosAluno,
    AtendimentosCandidato, AtendimentosInscrito, AtendimentosExAluno, StatusAtendimento
)
from core.utils import months, dic_tables


@login_required
def home(request):
    return render(request, 'home.html')


def dashboard(request):
    candidatos = Candidato.objects.all()
    inscritos = Inscrito.objects.all()
    alunos = Aluno.objects.all()
    exalunos = ExAluno.objects.all()
    context = {
        'qtd_candidatos': len(candidatos),
        'qtd_inscritos': len(inscritos),
        'qtd_alunos': len(alunos),
        'qtd_exalunos': len(exalunos)
    }
    return render(request, 'dashboard.html', context)


@login_required
def captacao(request):
    return render(request, 'base.html')


def candidatos(request):
    periodo = None
    filtro = request.POST.get('select-periodo')
    atendimentos = AtendimentosCandidato.objects.all()
    if filtro and not filtro == '0':
        periodo = Periodo.objects.get(pk=int(filtro))
        candidatos = Candidato.objects.filter(periodos=periodo, ativo=True)
    else:
        candidatos = Candidato.objects.filter(ativo=True)

    context = {
        'candidatos': candidatos,
        'form': CandidatoForm(request.POST or None),
        'periodos': Periodo.objects.all(),
        'filtro': periodo,
        'atendimentos': atendimentos,
    }
    return render(request, 'candidatos.html', context)


def modal_cria_candidato(request):
    form = CandidatoForm(request.POST or None)
    if form.is_valid():
        form.instance.criado_por = request.user
        form.save()
        form.instance.periodos.add(request.POST['periodo'])
        return redirect(reverse('candidatos'))
    return render(request, 'modal_cria_candidato.html', {'form': form})


def modal_atualiza_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    atendimentos = candidato.atendimentos_candidato.all()
    form = CandidatoForm(request.POST or None, instance=candidato)
    if form.is_valid():
        candidato.atualizado_por = request.user
        candidato.save()
        return redirect(reverse('candidatos'))
    context = {
        'form': form,
        'atendimentos': atendimentos,
        'periodos': candidato.periodos.all(),

        # 'cand': candidato.atendimentos_candidato.last().status.nome
    }
    return render(request, 'modal_atualiza_candidato.html', context)


def modal_remove_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    if request.POST:
        candidato.ativo = False
        candidato.save()
        return redirect(reverse('candidatos'))
    else:
        return render(request, 'modal_remove_candidato.html', {'candidato': candidato})


def inscritos(request):
    periodo = None
    filtro = request.POST.get('select-periodo')
    if filtro and not filtro == '0':
        periodo = Periodo.objects.get(pk=int(filtro))
        inscritos = Inscrito.objects.filter(periodos=periodo, ativo=True)
    else:
        inscritos = Inscrito.objects.filter(ativo=True)

    context = {
        'inscritos': inscritos,
        'form': InscritoForm(request.POST or None),
        'periodos': Periodo.objects.all(),
        'filtro': periodo
    }
    return render(request, 'inscritos.html', context)


def modal_cria_inscrito(request):
    form = InscritoForm(request.POST or None)
    if form.is_valid():
        form.instance.criado_por = request.user
        form.save()
        form.instance.periodos.add(request.POST['periodo'])
        return redirect(reverse('inscritos'))
    return render(request, 'modal_cria_inscrito.html', {'form': form})


def modal_atualiza_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    atendimentos = inscrito.atendimentos_inscrito.all()
    form = InscritoForm(request.POST or None, instance=inscrito)
    if form.is_valid():
        inscrito.atualizado_por = request.user
        inscrito.save()
        return redirect(reverse('inscritos'))
    context = {
        'form': form,
        'atendimentos': atendimentos,
        'periodos': inscrito.periodos.all()
    }
    return render(request, 'modal_atualiza_inscrito.html', context)


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


# def modal_cria_exaluno(request):
#     form = ExAlunoForm(request.POST or None)
#     if form.is_valid():
#         form.instance.criado_por = request.user
#         form.save()
#         return redirect(reverse('exalunos'))
#     return render(request, 'modal_cria_exaluno.html', {'form': form})


def modal_atualiza_exaluno(request, pk):
    exaluno = get_object_or_404(ExAluno, pk=pk)
    atendimentos = exaluno.atendimentos_exaluno.all()
    form = ExAlunoForm(request.POST or None, instance=exaluno)
    if form.is_valid():
        exaluno.atualizado_por = request.user
        exaluno.save()
        return redirect(reverse('exalunos'))
    context = {
        'form': form,
        'atendimentos': atendimentos,
        'periodos': exaluno.periodos.all()
    }
    return render(request, 'modal_atualiza_exaluno.html', context)


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


# def modal_cria_aluno(request):
#     form = AlunoForm(request.POST or None)
#     if form.is_valid():
#         form.instance.criado_por = request.user
#         form.save()
#         return redirect(reverse('alunos'))
#     return render(request, 'modal_cria_aluno.html', {'form': form})


def modal_atualiza_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    atendimentos = aluno.atendimentos_aluno.all()
    form = AlunoForm(request.POST or None, instance=aluno)
    if form.is_valid():
        aluno.atualizado_por = request.user
        aluno.save()
        return redirect(reverse('alunos'))
    context = {
        'form': form,
        'atendimentos': atendimentos,
        'periodos': aluno.periodos.all()
    }
    return render(request, 'modal_atualiza_aluno.html', context)


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
        nome = request.GET.get('novo_nome', None)
        h4_text = request.GET.get('h4_text', None)
        obj = dic_tables[h4_text].objects.create(nome=nome)
        select_id = unicodedata.normalize("NFD", h4_text.lower().split()[0]).encode("ascii", "ignore").decode("utf-8")
        novo = {'id': obj.id, 'nome': obj.nome, 'h4_text': h4_text, 'select_id': f'#id_{select_id}'}
        data = {'novo': novo}
        return JsonResponse(data)


class CreateNewCandidatoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        candidato_id = request.GET.get('candidato', None)
        status_id = request.GET.get('statusId', None)
        if descricao and candidato_id and status_id:
            candidato = Candidato.objects.get(pk=int(candidato_id))
            status = StatusAtendimento.objects.get(pk=int(status_id))
            obj = AtendimentosCandidato.objects.create(
                descricao=descricao,
                candidato=candidato,
                atendente=request.user,
                status=status
            )
            obj_data = f'{obj.data.day} de {months[obj.data.month]} de {obj.data.year} às {obj.data.time().strftime("%H:%M")}'
            data = {
                'data': obj_data,
                'descricao': obj.descricao,
                'atendente': obj.atendente.first_name or obj.atendente.username,
                'status': obj.status.nome
            }
            candidato.status_atendimento = status.nome
            candidato.save()
            return JsonResponse(data)
        return JsonResponse({})


class CreateNewInscritoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        inscrito_id = request.GET.get('inscrito', None)
        if descricao and inscrito_id:
            inscrito = Inscrito.objects.get(pk=int(inscrito_id))
            obj = AtendimentosInscrito.objects.create(descricao=descricao, inscrito=inscrito)
            obj_data = f'{obj.data.day} de {months[obj.data.month]} de {obj.data.year} às {obj.data.time().strftime("%H:%M")}'
            data = {'data': obj_data, 'descricao': obj.descricao}
            return JsonResponse(data)
        return JsonResponse({})


class CreateNewExalunoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        exaluno_id = request.GET.get('exaluno', None)
        if descricao and exaluno_id:
            exaluno = ExAluno.objects.get(pk=int(exaluno_id))
            obj = AtendimentosExAluno.objects.create(descricao=descricao, exaluno=exaluno)
            obj_data = f'{obj.data.day} de {months[obj.data.month]} de {obj.data.year} às {obj.data.time().strftime("%H:%M")}'
            data = {'data': obj_data, 'descricao': obj.descricao}
            return JsonResponse(data)
        return JsonResponse({})


class CreateNewAlunoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        aluno_id = request.GET.get('aluno', None)
        if descricao and aluno_id:
            aluno = Aluno.objects.get(pk=int(aluno_id))
            obj = AtendimentosAluno.objects.create(descricao=descricao, aluno=aluno)
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


def attendances(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    # atendimentos = candidato.atendimentos_candidato.all()
    # form = CandidatoForm(request.POST or None, instance=candidato)
    status_form = AtendimentosCandidatoForm()
    # if form.is_valid():
    #     candidato.atualizado_por = request.user
    #     candidato.save()
    #     return redirect(reverse('candidatos'))
    context = {
        # 'form': form,
        'candidato': candidato,
        # 'atendimentos': atendimentos,
        'status_form': status_form,

        # 'cand': candidato.atendimentos_candidato.last().status.nome
    }
    return render(request, 'attendances.html', context)

