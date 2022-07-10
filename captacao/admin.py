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
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(SituacaoInscrito)
class SituacaoInscritoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(SituacaoExAluno)
class SituacaoExAlunoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Motivo)
class MotivoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Marketing)
class MarketingAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Polo)
class PoloAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'nome_abrev']
    search_fields = ['nome', 'nome_abrev']
    list_filter = ['nome', 'nome_abrev']


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'marketing', 'status',
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

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


@admin.register(Inscrito)
class InscritoAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'status',
                    'data_contato', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'status']

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


@admin.register(ExAluno)
class ExAlunoAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'situacao', 'data_saida', 'motivo',
                    'status', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'status']

    def save_model(self, request, obj, form, change):
        salva_criado_por(request, obj)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = [
        # 'nom_campus',
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
        # 'periodos',
    ]
    search_fields = [
        'nom_campus',
        'nom_curso_grupo',
        'cod_curso',
        'tipo',
        'dsc_modalidade',
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
        # 'periodos',
    ]
    list_filter = [
        'nom_campus',
        'nom_curso_grupo',
        'cod_curso',
        'tipo',
        'dsc_modalidade',
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
        # 'periodos',
    ]
    # readonly_fields = ['polo__nome_abrev', 'curso__nome_abrev', 'turma_ano_ingresso_abrev']
    # readonly_fields = ['nom_campus_abrev', 'nom_curso_grupo_abrev', 'turma_ano_ingresso_abrev']
    # def save_model(self, request, obj, form, change):
    #     salva_criado_por(request, obj)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path(
                'botao-da-app/',
                # self.admin_site.admin_view(self.minha_funcao_category, cacheable=True)
                self.admin_site.admin_view(self.import_xlsx, cacheable=True)
            ),
        ]
        return my_urls + urls

    def minha_funcao_category(self, request):
        print('Ao clicar no botão, faz alguma coisa em category...')
        messages.add_message(
            request,
            messages.INFO,
            'Ação realizada com sucesso.'
        )
        return redirect('admin:captacao_aluno_changelist')

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
                field_names = [{field.verbose_name: field.name} for field in meta.fields]
                file = request.FILES['files']
                df_file = pd.read_excel(file, 0, index_col=None)
                df = df_file[aluno_fields]
                df.columns = aluno_fields
                replace_columns = []
                for column in df.columns:
                    for name in field_names:
                        column = name.get(column.replace('?', ''), column)
                    replace_columns.append(column)
                df.columns = replace_columns
                students = df.to_dict(orient='index')
                for student in students.values():
                    # TODO Ver essa lógica
                    campus = self.get_campus(student['nom_campus'])
                    curso = self.get_curso(student['nom_curso_grupo'])
                    modalidade = self.get_modalidade(student['dsc_modalidade'])
                    turma_ano_ingresso_abrev = student['turma_ano_ingresso'].split()[-1].replace('/', ' de ')

                    student['nom_campus'] = campus
                    student['nom_curso_grupo'] = curso
                    student['dsc_modalidade'] = modalidade
                    student['turma_ano_ingresso_abrev'] = turma_ano_ingresso_abrev

                    student['dat_matr'] = self.format_date(student['dat_matr'])
                    student['dat_ingresso'] = self.format_date(student['dat_ingresso'])
                    student['data_prev_termino'] = self.format_date(student['data_prev_termino'])

                    # if isinstance(student['cod_curso'], int):
                    #     student['cod_curso'] = student['cod_curso']
                    # else:
                    #     student['cod_curso'] = 0
                    Aluno.objects.update_or_create(
                        # nom_aluno=student['nom_aluno'],
                        cod_ra=student['cod_ra'],
                        defaults=student)
                # print(f'{settings.BASE_DIR}/{path}')
                messages.add_message(
                    request,
                    messages.INFO,
                    'Arquivo lido com sucesso. A tabela de alunos foi atualizada.'
                )
            except Exception as error:
                messages.add_message(
                    request,
                    messages.ERROR,
                    f'Erro na leitura do arquivo. Certifique-se que o arquivo contém os dados dos alunos. {error}'
                )

            return redirect('admin:captacao_aluno_changelist')
        # return render(request, 'upload_file.html')
        return render(request, 'modal_cria_aluno.html')

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
