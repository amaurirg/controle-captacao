from datetime import datetime, date

import pandas as pd
from django.conf import settings
from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from captacao.models import (Status, Marketing, Curso, Polo, Candidato, Periodo, Atendente, Motivo, Inscrito,
                             ExAluno, SituacaoInscrito, SituacaoExAluno, Aluno, Modalidade)
from core.utils import export_xlsx, export_as_csv, salva_criado_por, aluno_fields


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(SituacaoInscrito)
class SituacaoInscritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(SituacaoExAluno)
class SituacaoExAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Motivo)
class MotivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Polo)
class PoloAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'marketing', 'status',
                    'data_contato', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'marketing__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'marketing', 'status']

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)
        # if not obj.pk:
        #     obj.atendente = request.user
        # # obj.save()
        # super(CandidatoAdmin, self).save_model(request, obj, form, change)

    actions = (export_as_csv, export_xlsx)


@admin.register(Inscrito)
class InscritoAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'status',
                    'data_contato', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'status']

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)

    actions = (export_as_csv, export_xlsx)


@admin.register(ExAluno)
class ExAlunoAdmin(admin.ModelAdmin):
    list_display = ['id', 'periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'situacao', 'data_saida', 'motivo',
                    'status', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'status']

    # def save_model(self, request, obj, form, change):
    #     salva_criado_por(request, obj)

    actions = (export_as_csv, export_xlsx)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'inserir-arquivo/',
                # self.admin_site.admin_view(self.minha_funcao_category, cacheable=True)
                self.admin_site.admin_view(self.import_xlsx, cacheable=True)
            ),
        ]
        return my_urls + urls

    # def minha_funcao_category(self, request):
    #     print('Ao clicar no botão, faz alguma coisa em category...')
    #     messages.add_message(
    #         request,
    #         messages.INFO,
    #         'Ação realizada com sucesso.'
    #     )
    #     return redirect('admin:captacao_aluno_changelist')

    def get_campus(self, campus):
        obj_nom_campus, created = Polo.objects.get_or_create(
            nome=campus, defaults={'nome_abrev': campus}
        )
        return obj_nom_campus

    def polo_nome_abrev(self, obj):
        return obj.nom_campus.nome_abrev

    def curso_nome_abrev(self, obj):
        return obj.nom_curso_grupo.nome_abrev

    def modalidade_nome_abrev(self, obj):
        return obj.dsc_modalidade.nome_abrev

    def get_curso(self, curso):
        obj_nom_curso, created = Curso.objects.get_or_create(
            nome=curso, defaults={'nome_abrev': curso}
        )
        return obj_nom_curso

    def get_modalidade(self, modalidade):
        obj_modalidade, created = Modalidade.objects.get_or_create(
            nome=modalidade, defaults={'nome_abrev': modalidade}
        )
        return obj_modalidade

    def format_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d/%m/%Y').date()
        except:
            return date(1111, 11, 11)


    def import_xlsx(self, request):
        if request.method == 'POST':
            try:
                meta = self.model._meta
                field_names = {}
                for field in meta.fields:
                    field_names[field.verbose_name] = field.name
                select_periodo = int(request.POST.get('select-periodo'))
                periodo = Periodo.objects.get(pk=select_periodo)
                file = request.FILES['files']
                df_file = pd.read_excel(file, 0, index_col=None)
                df = df_file[aluno_fields]
                df.rename(columns={'Bolsista?': 'Bolsista'}, inplace=True)
                df.rename(columns=field_names, inplace=True)

                students = df.to_dict(orient='index')
                for student in students.values():
                    campus = self.get_campus(student['nom_campus'].rstrip())
                    curso = self.get_curso(student['nom_curso_grupo'].rstrip())
                    modalidade = self.get_modalidade(student['dsc_modalidade'].rstrip())

                    student['nom_campus'] = campus
                    student['nom_curso_grupo'] = curso
                    student['dsc_modalidade'] = modalidade

                    student['dat_matr'] = self.format_date(student['dat_matr'])
                    student['dat_ingresso'] = self.format_date(student['dat_ingresso'])
                    student['data_prev_termino'] = self.format_date(student['data_prev_termino'])

                    data = student['turma_ano_ingresso'].split()[-1]
                    mes, ano = data.split('/')
                    turma_ano_ingresso_abrev = f'{mes[:3]}/{ano[-2:]}'
                    student['turma_ano_ingresso_abrev'] = turma_ano_ingresso_abrev.rstrip()

                    student['status_aluno'] = student['status_aluno'].rstrip()
                    if student['status_aluno'] == 'Transferência de out':
                        student['status_aluno'] = 'Transf. de out'

                    student['turma_ano_ingresso'] = student['turma_ano_ingresso'].rstrip()
                    student['cidade'] = student['cidade'].rstrip()
                    student['bairro'] = student['bairro'].rstrip()
                    student['bolsista'] = student['bolsista'].rstrip()
                    student['email'] = student['email'].rstrip()

                    exaluno, created = ExAluno.objects.update_or_create(
                        ra=student['cod_ra'],
                        defaults=student)
                    exaluno.periodos.add(periodo)
                messages.add_message(
                    request,
                    messages.INFO,
                    'Arquivo lido com sucesso. A tabela de alunos foi atualizada.'
                )
            except Exception as error:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Erro na leitura do arquivo. Certifique-se que o arquivo contém os dados dos alunos.'
                )

            return redirect('admin:captacao_exaluno_changelist')
        return render(request, 'modal_cria_exaluno.html', {'periodos': Periodo.objects.all()})


class PeriodoInline(admin.TabularInline):
    model = Aluno.periodos.through
    extra = 0


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']

    inlines = (PeriodoInline,)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'polo_nome_abrev',
        'nom_curso_grupo',
        'curso_nome_abrev',
        'cod_curso',
        'tipo',
        'dsc_modalidade',
        'modalidade_nome_abrev',
        'serie',
        'semana',
        'cod_ra',
        'nom_aluno',
        'dat_matr',
        'status_aluno',
        'turma_ano_ingresso',
        'turma_ano_ingresso_abrev',
        'email',
        'telefone1',
        'telefone2',
        'telefone_res',
        'cidade',
        'bairro',
        'bolsista',
        'dat_ingresso',
        'data_prev_termino',
        'ativo',
        'todos_periodos'
    ]
    search_fields = [
        'nom_campus__nome_abrev',
        'nom_curso_grupo__nome_abrev',
        'cod_curso',
        'tipo',
        'dsc_modalidade__nome_abrev',
        'serie',
        'semana',
        'cod_ra',
        'nom_aluno',
        'dat_matr',
        'status_aluno',
        'turma_ano_ingresso',
        'email',
        'telefone1',
        'telefone2',
        'telefone_res',
        'cidade',
        'bairro',
        'bolsista',
        'dat_ingresso',
        'data_prev_termino',
        'ativo',
    ]

    list_filter = [
        'bolsista',
        'ativo',
        'tipo',
        'nom_campus__nome_abrev',
        'nom_curso_grupo',
        'dsc_modalidade',
        'serie',
        'semana',
        'status_aluno',
        'turma_ano_ingresso_abrev',
        'cidade',
        'bairro',
    ]

    def todos_periodos(self, obj):
        lista = []
        for periodo in obj.periodos.all():
            lista.append(periodo)
        return lista

    inlines = (PeriodoInline,)
    readonly_fields = ['periodos']

    # def save_model(self, request, obj, form, change):
    #     salva_criado_por(request, obj)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'inserir-arquivo/',
                # self.admin_site.admin_view(self.minha_funcao_category, cacheable=True)
                self.admin_site.admin_view(self.import_xlsx, cacheable=True)
            ),
        ]
        return my_urls + urls

    # def minha_funcao_category(self, request):
    #     print('Ao clicar no botão, faz alguma coisa em category...')
    #     messages.add_message(
    #         request,
    #         messages.INFO,
    #         'Ação realizada com sucesso.'
    #     )
    #     return redirect('admin:captacao_aluno_changelist')

    def get_campus(self, campus):
        obj_nom_campus, created = Polo.objects.get_or_create(
            nome=campus, defaults={'nome_abrev': campus}
        )
        return obj_nom_campus

    def polo_nome_abrev(self, obj):
        return obj.nom_campus.nome_abrev

    def curso_nome_abrev(self, obj):
        return obj.nom_curso_grupo.nome_abrev

    def modalidade_nome_abrev(self, obj):
        return obj.dsc_modalidade.nome_abrev

    def get_curso(self, curso):
        obj_nom_curso, created = Curso.objects.get_or_create(
            nome=curso, defaults={'nome_abrev': curso}
        )
        return obj_nom_curso

    def get_modalidade(self, modalidade):
        obj_modalidade, created = Modalidade.objects.get_or_create(
            nome=modalidade, defaults={'nome_abrev': modalidade}
        )
        return obj_modalidade

    def format_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d/%m/%Y').date()
        except:
            return date(1111, 11, 11)


    def import_xlsx(self, request):
        if request.method == 'POST':
            try:
                meta = self.model._meta
                field_names = {}
                for field in meta.fields:
                    field_names[field.verbose_name] = field.name
                select_periodo = int(request.POST.get('select-periodo'))
                periodo = Periodo.objects.get(pk=select_periodo)
                file = request.FILES['files']
                df_file = pd.read_excel(file, 0, index_col=None)
                df = df_file[aluno_fields]
                df.rename(columns={'Bolsista?': 'Bolsista'}, inplace=True)
                df.rename(columns=field_names, inplace=True)

                students = df.to_dict(orient='index')
                for student in students.values():
                    campus = self.get_campus(student['nom_campus'].rstrip())
                    curso = self.get_curso(student['nom_curso_grupo'].rstrip())
                    modalidade = self.get_modalidade(student['dsc_modalidade'].rstrip())

                    student['nom_campus'] = campus
                    student['nom_curso_grupo'] = curso
                    student['dsc_modalidade'] = modalidade

                    student['dat_matr'] = self.format_date(student['dat_matr'])
                    student['dat_ingresso'] = self.format_date(student['dat_ingresso'])
                    student['data_prev_termino'] = self.format_date(student['data_prev_termino'])

                    data = student['turma_ano_ingresso'].split()[-1]
                    mes, ano = data.split('/')
                    turma_ano_ingresso_abrev = f'{mes[:3]}/{ano[-2:]}'
                    student['turma_ano_ingresso_abrev'] = turma_ano_ingresso_abrev.rstrip()

                    student['status_aluno'] = student['status_aluno'].rstrip()
                    if student['status_aluno'] == 'Transferência de out':
                        student['status_aluno'] = 'Transf. de out'

                    student['turma_ano_ingresso'] = student['turma_ano_ingresso'].rstrip()
                    student['cidade'] = student['cidade'].rstrip()
                    student['bairro'] = student['bairro'].rstrip()
                    student['bolsista'] = student['bolsista'].rstrip()
                    student['email'] = student['email'].rstrip()

                    aluno, created = Aluno.objects.update_or_create(
                        cod_ra=student['cod_ra'],
                        defaults=student)
                    aluno.periodos.add(periodo)
                messages.add_message(
                    request,
                    messages.INFO,
                    'Arquivo lido com sucesso. A tabela de alunos foi atualizada.'
                )
            except Exception:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Erro na leitura do arquivo. Certifique-se que o arquivo contém os dados dos alunos.'
                )

            return redirect('admin:captacao_aluno_changelist')
        return render(request, 'modal_cria_aluno.html', {'periodos': Periodo.objects.all()})


    # def read_file(filename, **kwargs):
    #
    #     """Read file with **kwargs; files supported: xls, xlsx, csv, csv.gz, pkl"""
    #
    #     read_map = {'xls': pd.read_excel, 'xlsx': pd.read_excel, 'csv': pd.read_csv,
    #                 'gz': pd.read_csv, 'pkl': pd.read_pickle}
    #
    #     ext = os.path.splitext(filename)[1].lower()[1:]
    #     assert ext in read_map, "Input file not in correct format, must be xls, xlsx, csv, csv.gz, pkl; current format '{0}'".format(ext)
    #     assert os.path.isfile(filename), "File Not Found Exception '{0}'.".format(filename)
    #
    #     return read_map[ext](filename, **kwargs)


export_xlsx.short_description = "Exportar dados em formato Excel"
export_as_csv.short_description = "Exportar dados em formato CSV"
