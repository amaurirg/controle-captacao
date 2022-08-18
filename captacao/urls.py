from django.urls import path, include
from .views import (
    periodos, CreateNewName,
    candidatos, modal_cria_candidato, modal_atualiza_candidato, modal_remove_candidato,
    inscritos, modal_cria_inscrito, modal_atualiza_inscrito, modal_remove_inscrito,
    exalunos, modal_atualiza_exaluno, modal_remove_exaluno, alunos, modal_atualiza_aluno,
    CreateNewCandidatoAttendance, CreateNewInscritoAttendance, CreateNewExalunoAttendance,
    CreateNewAlunoAttendance, attendances
)

urlpatterns = [
    path('create/name', CreateNewName.as_view(), name='create_new_name'),
    path('create/candidato/attendance', CreateNewCandidatoAttendance.as_view(), name='create_candidato_attendance'),
    path('create/inscrito/attendance', CreateNewInscritoAttendance.as_view(), name='create_inscrito_attendance'),
    path('create/exaluno/attendance', CreateNewExalunoAttendance.as_view(), name='create_exaluno_attendance'),
    path('create/aluno/attendance', CreateNewAlunoAttendance.as_view(), name='create_aluno_attendance'),
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
    path('atualizar_exaluno/<int:pk>', modal_atualiza_exaluno, name='modal_atualiza_exaluno'),
    path('remover_exaluno/<int:pk>', modal_remove_exaluno, name='modal_remove_exaluno'),

    path('alunos/', alunos, name="alunos"),
    path('atualizar_aluno/<int:pk>', modal_atualiza_aluno, name='modal_atualiza_aluno'),

    path('attendances/<int:pk>', attendances, name='attendances')
]
