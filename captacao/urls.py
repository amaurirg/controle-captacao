from django.urls import path
from .views import captacao

urlpatterns = [
    path('', captacao, name="captacao"),
]
