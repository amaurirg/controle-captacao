from django.urls import path
from .views import (captacao, modal_cria_candidato, candidatos, inscritos, exalunos, modal_atualiza_candidato,
                    modal_remove_candidato)

urlpatterns = [
    path('', captacao, name="captacao"),
    path('candidatos/', candidatos, name="candidatos"),
    path('inscritos/', inscritos, name="inscritos"),
    path('ex-alunos/', exalunos, name="ex-alunos"),
    path('adicionar_candidato/', modal_cria_candidato, name='modal_cria_candidato'),
    path('atualizar_candidato/<int:pk>', modal_atualiza_candidato, name='modal_atualiza_candidato'),
    path('remover_candidato/<int:pk>', modal_remove_candidato, name='modal_remove_candidato')
]
