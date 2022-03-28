from django.urls import path
from .views import captacao, modal_cria_candidato

urlpatterns = [
    path('', captacao, name="captacao"),
    path('adicionar/', modal_cria_candidato, name='adicionar')
]
