import csv
from django.http import HttpResponse
import pandas as pd

from captacao.models import Periodo, Polo, Curso, Marketing, Status, SituacaoInscrito, SituacaoExAluno, Motivo

cursos = {
    # 'Administração': '',
    # 'Arquitetura e Urbanismo': '',
    # 'Artes Visuais': '',
    # 'Biomedicina': '',
    # 'Ciências Biológicas': '',
    # 'Ciências Contábeis': '',
    # 'Engenharia Ambiental': '',
    # 'Educação Física': '',
    # 'Engenharia Civil': '',
    # 'Engenharia de Computação': '',
    # 'Engenharia de Produção': '',
    # 'Engenharia de Software': '',
    # 'Engenharia Elétrica': '',
    # 'Engenharia Mecânica': '',
    # 'Engenharia Química': '',
    # 'Filosofia': '',
    # 'Fisioterapia': '',
    # 'Geografia': '',
    # 'História': '',
    # 'Letras': '',
    # 'Matemática': '',
    # 'Nutrição': '',
    # 'Pedagogia': '',
    # 'Psicopedagogia': '',
    # 'Serviço Social': '',
    'Superior de Tecnologia em Análise e Desenvolvimento de Sistemas': 'ADS',
    'Superior de Tecnologia em Design de Interiores': 'Design de Interiores',
    'Superior de Tecnologia em Estética e Cosmética': 'Estética e Cosmética',
    'Superior de Tecnologia em Gastronomia': 'Gastronomia',
    'Superior de Tecnologia em Gestão Ambiental': 'Gestão Ambiental',
    'Superior de Tecnologia em Gestão Comercial': 'Gestão Comercial',
    'Superior de Tecnologia em Gestão da Qualidade': 'Gestão da Qualidade',
    'Superior de Tecnologia em Gestão da Tecnologia da Informação': 'TI',
    'Superior de Tecnologia em Gestão Financeira': 'Gestão Financeira',
    'Superior de Tecnologia em Gestão de Recursos Humanos': 'Gestão de Recursos Humanos',
    'Superior de Tecnologia em Gestão de Segurança Privada': 'Gestão de Segurança Privada',
    'Superior de Tecnologia em Logística': 'Logística',
    'Superior de Tecnologia em Gestão Pública': 'Gestão Pública',
    'Superior de Tecnologia em Gestão Hospitalar': 'Gestão Hospitalar',
    'Superior de Tecnologia em Marketing': 'Marketing',
    'Superior de Tecnologia em Processos Escolares': 'Processos Escolares',
    'Superior de Tecnologia em Marketing Digital': 'Marketing Digital',
    'Superior de Tecnologia em Processos Gerenciais': 'Processos Gerenciais',
    'Superior de Tecnologia em Segurança no Trabalho': 'Segurança no Trabalho',
    'Superior de Tecnologia em Serviços Jurídicos, Cartorários e Notariais': 'Serv. Jur. Car. Notariais',
}

aluno_fields = [
    'NomCampus',
    'NomCursoGrupo',
    'CodCurso',
    'Tipo',
    'DscModalidade',
    'Serie',
    'Semana',
    'CodRA',
    'NomAluno',
    'DatMatr',
    'StatusAluno',
    'TurmaAnoIngresso',
    'Email',
    'TelefoneCel1',
    'TelefoneCel2',
    'TelefoneRes',
    'Cidade',
    'Bairro',
    'Bolsista?',
    'Dat_ingresso',
    'DataPrevTermino',
]

exaluno_fields = [
    'NomCampus',
    'NomAluno',
    'CodRA',
    'DscModalidade',
    'NomCursoGrupo',
    'DscStatusMatr',
    'TurmaAnoIngresso',
    'Email',
    'TelefoneCel1',
    'TelefoneCel2',
    'TelefoneRes',
]

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


def salva_criado_por(request, obj):
    if not obj.pk:
        obj.criado_por = request.user
    else:
        obj.atualizado_por = request.user
    obj.save()


def export_as_csv(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)
    writer.writerow(field_names)
    for obj in queryset:
        # obj.criado_em = obj.criado_em.strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([getattr(obj, field) for field in field_names])
    return response


def export_xlsx(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    data = []

    for obj in queryset:
        dic = {}
        for field in field_names:
            dic[field] = getattr(obj, field)
        data.append(dic)

    pd.DataFrame(data).to_excel('/tmp/output.xlsx', index=False)
