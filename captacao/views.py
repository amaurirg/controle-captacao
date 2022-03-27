from django.shortcuts import render

from captacao.models import Candidato, Periodo, Status, Marketing, Polo


def captacao(request):
    candidatos = Candidato.objects.all()
    fields_names = [field for field in candidatos.model._meta.fields]

    context = {
        'candidatos': candidatos,
        'fields_names': fields_names,
        'periodos': Periodo.objects.all(),
        'polos': Polo.objects.all(),
        'marketing_list': Marketing.objects.all(),
        'status_list': Status.objects.all()
    }
    return render(request, 'captacao.html', context)
