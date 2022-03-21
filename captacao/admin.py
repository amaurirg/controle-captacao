from django.contrib import admin

from captacao.models import Status, Marketing, Curso, Polo, Candidato, Periodo
from core.utils import export_xlsx, export_as_csv, salva_criado_por


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


# @admin.register(Atendente)
# class AtendenteAdmin(admin.ModelAdmin):
#     list_display = ['nome']
#     search_fields = ['nome']
#     list_filter = ['nome']


@admin.register(Polo)
class PoloAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
    list_filter = ['nome']


@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ['periodo', 'polo', 'nome', 'telefone1', 'email', 'curso', 'marketing', 'status',
                    'data_contato', 'observacoes']
    search_fields = ['periodo__nome', 'polo__nome', 'nome', 'telefone1', 'telefone2', 'email', 'data_contato',
                     'curso__nome', 'marketing__nome', 'status__nome']
    list_filter = ['periodo', 'polo', 'marketing', 'status']

    def save_model(self, request, obj, form, change):
        # salva_criado_por(request, obj)
        if not obj.pk:
            obj.atendente = request.user
        # obj.save()
        super(CandidatoAdmin, self).save_model(request, obj, form, change)

    # actions = export_xlsx
    actions = (export_as_csv, export_xlsx)


export_xlsx.short_description = "Exportar dados em formato Excel"
export_as_csv.short_description = "Exportar dados em formato CSV"
