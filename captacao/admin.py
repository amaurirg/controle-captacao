from django.contrib import admin

from captacao.models import (Status, Marketing, Curso, Polo, Candidato, Periodo, Atendente, Motivo, Inscrito,
                             ExAluno, SituacaoInscrito, SituacaoExAluno, Aluno, Modalidade)
from core.utils import export_xlsx, export_as_csv, salva_criado_por


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
        'nom_campus',
        'nom_campus_abrev',
        'nom_curso_grupo',
        'nom_curso_grupo_abrev',
        'cod_curso',
        'tipo',
        'dsc_modalidade',
        'dsc_modalidade_abrev',
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
    readonly_fields = ['nom_campus_abrev', 'nom_curso_grupo_abrev', 'turma_ano_ingresso_abrev']
    # def save_model(self, request, obj, form, change):
    #     salva_criado_por(request, obj)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


export_xlsx.short_description = "Exportar dados em formato Excel"
export_as_csv.short_description = "Exportar dados em formato CSV"
