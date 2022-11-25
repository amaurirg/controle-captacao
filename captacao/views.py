import json
import unicodedata
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import View

from captacao.forms import CandidatoForm, InscritoForm, AlunoForm, ExAlunoForm, AtendimentosCandidatoForm, \
    AtendimentosInscritoForm, AtendimentosAlunoForm, AtendimentosExAlunoForm
from captacao.models import (
    Candidato, Periodo, Inscrito, Aluno, ExAluno, AtendimentosAluno,
    AtendimentosCandidato, AtendimentosInscrito, AtendimentosExAluno, StatusAtendimento, UserProfile, EmailFile
)
from core.utils import months, dic_tables


@login_required
def home(request):
    return render(request, 'home.html')


def dashboard(request):
    candidatos = Candidato.objects.all().count()
    inscritos = Inscrito.objects.all().count()
    alunos = Aluno.objects.all().count()
    exalunos = ExAluno.objects.all().count()
    context = {
        'qtd_candidatos': candidatos,
        'qtd_inscritos': inscritos,
        'qtd_alunos': alunos,
        'qtd_exalunos': exalunos
    }
    return render(request, 'dashboard.html', context)


def relatorio_candidatos(request):
    periodos = Periodo.objects.values('nome').annotate(total=Count('periodos_candidato')).order_by('-nome')[:8][::-1]
    data = {'data': [], 'labels': []}
    for periodo in periodos:
        data['data'].append(periodo['total'])
        data['labels'].append(periodo['nome'])
    print(data)
    return JsonResponse(data)


def relatorio_inscritos(request):
    periodos = Periodo.objects.values('nome').annotate(total=Count('periodos_inscrito')).order_by('-nome')[:8][::-1]
    data = {'data': [], 'labels': []}
    for periodo in periodos:
        data['data'].append(periodo['total'])
        data['labels'].append(periodo['nome'])
    print(data)
    return JsonResponse(data)


def relatorio_alunos(request):
    periodos = Periodo.objects.values('nome').annotate(total=Count('periodos_aluno')).order_by('-nome')[:8][::-1]
    data = {'data': [], 'labels': []}
    for periodo in periodos:
        data['data'].append(periodo['total'])
        data['labels'].append(periodo['nome'])
    print(data)
    return JsonResponse(data)


def relatorio_exalunos(request):
    periodos = Periodo.objects.values('nome').annotate(total=Count('periodos_exaluno')).order_by('-nome')[:8][::-1]
    data = {'data': [], 'labels': []}
    for periodo in periodos:
        data['data'].append(periodo['total'])
        data['labels'].append(periodo['nome'])
    print(data)
    return JsonResponse(data)


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
        status_id = request.GET.get('statusId', None)
        if descricao and inscrito_id and status_id:
            inscrito = Inscrito.objects.get(pk=int(inscrito_id))
            status = StatusAtendimento.objects.get(pk=int(status_id))
            obj = AtendimentosInscrito.objects.create(
                descricao=descricao,
                inscrito=inscrito,
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
            inscrito.status_atendimento = status.nome
            inscrito.save()
            return JsonResponse(data)
        return JsonResponse({})


class CreateNewExalunoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        exaluno_id = request.GET.get('exaluno', None)
        status_id = request.GET.get('statusId', None)
        if descricao and exaluno_id and status_id:
            exaluno = ExAluno.objects.get(pk=int(exaluno_id))
            status = StatusAtendimento.objects.get(pk=int(status_id))
            obj = AtendimentosExAluno.objects.create(
                descricao=descricao,
                exaluno=exaluno,
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
            exaluno.status_atendimento = status.nome
            exaluno.save()
            return JsonResponse(data)
        return JsonResponse({})


class CreateNewAlunoAttendance(View):
    def get(self, request):
        descricao = request.GET.get('descricao', None)
        aluno_id = request.GET.get('aluno', None)
        status_id = request.GET.get('statusId', None)
        if descricao and aluno_id and status_id:
            aluno = Aluno.objects.get(pk=int(aluno_id))
            status = StatusAtendimento.objects.get(pk=int(status_id))
            obj = AtendimentosAluno.objects.create(
                descricao=descricao,
                aluno=aluno,
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
            aluno.status_atendimento = status.nome
            aluno.save()
            return JsonResponse(data)
        return JsonResponse({})


def periodos(request):
    periodos = Periodo.objects.filter(ativo=True)
    context = {
        'periodos': periodos
    }
    return render(request, 'periodos.html', context)


def atendimentos_candidato(request, pk):
    candidato = get_object_or_404(Candidato, pk=pk)
    status_form = AtendimentosCandidatoForm()
    context = {
        'candidato': candidato,
        'status_form': status_form,
    }
    return render(request, 'atendimentos_candidato.html', context)


def atendimentos_inscrito(request, pk):
    inscrito = get_object_or_404(Inscrito, pk=pk)
    status_form = AtendimentosInscritoForm()
    context = {
        'inscrito': inscrito,
        'status_form': status_form,
    }
    return render(request, 'atendimentos_inscrito.html', context)


def atendimentos_exaluno(request, pk):
    exaluno = get_object_or_404(ExAluno, pk=pk)
    status_form = AtendimentosExAlunoForm()
    context = {
        'exaluno': exaluno,
        'status_form': status_form,
    }
    return render(request, 'atendimentos_exaluno.html', context)


def atendimentos_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    status_form = AtendimentosAlunoForm()
    context = {
        'aluno': aluno,
        'status_form': status_form,
    }
    return render(request, 'atendimentos_aluno.html', context)


def upload_photo(request):
    if request.method == 'POST':
        photo = request.FILES.get('photoUser')
        new_photo, created = UserProfile.objects.update_or_create(
            profile=request.user,
            defaults={
                'filepath': photo
            }
        )
        return JsonResponse({'filepath': str(new_photo.filepath)})
    return render(request, 'upload_photo.html')


def envia_email(request, pk):
    email = EmailFile.objects.get(pk=pk)
    data = json.loads(request.body)
    html_content = render_to_string(
        'emails/padrao.html',
        {
            # 'nome': request.user.get_full_name().title() or request.user.username,
            'texto': email.email
        }
    )
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        # subject='Testando o envio de emails',
        subject=data.get('assunto'),
        body=text_content,
        # body=html_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        # to=[settings.DEFAULT_FROM_EMAIL]
        to=data['emails']
    )

    email.attach_alternative(html_content, 'text/html')
    email.send()
    return HttpResponse('Email enviado')


def emails(request):
    emails = EmailFile.objects.all()
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            email = EmailFile.objects.create(filename=data['nome'], email=data['email'])
            return JsonResponse({
                'create': 'success',
                'id': email.pk,
                'nome': email.filename,
                'email': email.email,
            }, status=201)
        except:
            return JsonResponse({'erro': 'Nome inválido ou arquivo já existe'}, status=409)
    return render(request, 'emails.html', {'emails': emails})


def email_detail(request, pk):
    email = EmailFile.objects.get(pk=pk)
    return JsonResponse({'email': email.email})
