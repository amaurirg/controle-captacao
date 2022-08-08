from django.urls import path, include
from .views import (
    periodos, CreateNewName,
    candidatos, modal_cria_candidato, modal_atualiza_candidato, modal_remove_candidato,
    inscritos, modal_cria_inscrito, modal_atualiza_inscrito, modal_remove_inscrito,
    exalunos, modal_cria_exaluno, modal_atualiza_exaluno, modal_remove_exaluno,
    alunos, modal_atualiza_aluno, modal_cria_aluno, CreateNewAttendance
)

urlpatterns = [
    path('create/name', CreateNewName.as_view(), name='create_new_name'),
    path('create/attendance', CreateNewAttendance.as_view(), name='create_new_attendance'),
    path('periodos/', periodos, name='periodos'),

    path('candidatos/', candidatos, name="candidatos"),
    path('adicionar_candidato/', modal_cria_candidato, name='modal_cria_candidato'),
    path('atualizar_candidato/<int:pk>', modal_atualiza_candidato, name='modal_atualiza_candidato'),
    path('remover_candidato/<int:pk>', modal_remove_candidato, name='modal_remove_candidato'),

    path('inscritos/', inscritos, name="inscritos"),
    path('adicionar_inscrito/', modal_cria_inscrito, name='modal_cria_inscrito'),
    path('atualizar_inscrito/<int:pk>', modal_atualiza_inscrito, name='modal_atualiza_inscrito'),
    path('remover_inscrito/<int:pk>', modal_remove_inscrito, name='modal_remove_inscrito'),

    path('exalunos/', exalunos, name="exalunos"),
    path('adicionar_exaluno/', modal_cria_exaluno, name='modal_cria_exaluno'),
    path('atualizar_exaluno/<int:pk>', modal_atualiza_exaluno, name='modal_atualiza_exaluno'),
    path('remover_exaluno/<int:pk>', modal_remove_exaluno, name='modal_remove_exaluno'),

    path('alunos/', alunos, name="alunos"),
    path('adicionar_aluno/', modal_cria_aluno, name='modal_cria_aluno'),
    path('atualizar_aluno/<int:pk>', modal_atualiza_aluno, name='modal_atualiza_aluno'),
]
