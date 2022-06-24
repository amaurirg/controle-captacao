import csv
from datetime import datetime
from django.http import HttpResponse
import xlwt


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
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{meta}.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('meta')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in range(len(field_names)):
        ws.write(row_num, col_num, field_names[col_num], font_style)

    default_style = xlwt.XFStyle()
    rows = queryset.values_list()
    rows = [[x.strftime("%Y-%m-%d %H:%M:%S") if isinstance(x, datetime) else x for x in row] for row in rows]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], default_style)

    wb.save(response)
    return response


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

polos = {
    'Polo Educacional de Praia Grande - SP': 'Praia Grande'
}

modalidade = {
    'Bacharelado': 'Bac',
    'Licenciatura': 'Lic',
    'Tecnólogo': 'Tec',

}
