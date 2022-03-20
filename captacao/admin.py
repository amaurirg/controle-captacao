from django.contrib import admin

from captacao.models import Status, Marketing, Curso, Atendente, Polo, Candidato
from core.utils import export_xlsx, export_as_csv


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
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
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Atendente)
class AtendenteAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Polo)
class PoloAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['polo', 'nome', 'telefone1', 'telefone2', 'email', 'curso', 'marketing', 'status', 'atendente',
                    'data_contato', 'observacoes']
    search_fields = ['polo', 'nome', 'telefone1', 'telefone2', 'email', 'curso', 'marketing', 'status', 'atendente',
                     'data_contato']
    list_filter = ['polo', 'nome', 'telefone1', 'telefone2', 'email', 'curso', 'marketing', 'status', 'atendente',
                   'data_contato']

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


export_xlsx.short_description = "Exportar dados em formato Excel"
export_as_csv.short_description = "Exportar dados em formato CSV"
