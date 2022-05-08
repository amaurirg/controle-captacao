from django import forms
from .models import Candidato, Inscrito, ExAluno, Periodo


class CandidatoForm(forms.ModelForm):
    class Meta:
        fields = [
            'periodo',
            'polo',
            'curso',
            'marketing',
            'nome',
            'email',
            'telefone1',
            'telefone2',
            'data_contato',
            'status',
            'atendente',
            'observacoes',
        ]
        model = Candidato
        # fields = ['forma_pagto', 'vendedor']
        widgets = {
            'periodo': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Período',
            }),
            'polo': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Polo',
            }),
            'curso': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Curso',
            }),
            'marketing': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Marketing',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Nome',
            }),
            'email': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Email',
            }),
            'telefone1': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Telefone 1',
            }),
            'telefone2': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Telefone 2',
            }),
            'data_contato': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Data do contato',
            }),
            'status': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Status',
            }),
            'atendente': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Atendente',
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'ui input focus',
                'placeholder': 'Observações',
                'rows': 6
            }),

        }


class PeriodoForm(forms.ModelForm):
    class Meta:
        model = Periodo
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Digite um novo período',
            })
        }

# class InscritoForm(forms.ModelForm):
#     class Meta:
#         fields = [
#             'periodo',
#             'polo',
#             'curso',
#             'nome',
#             'email',
#             'telefone1',
#             'telefone2',
#             'data_contato',
#             'atendente',
#             'status',
#             'situacao',
#             'observacoes',
#         ]
#         model = Inscrito
#         # fields = ['forma_pagto', 'vendedor']
#         widgets = {
#             'periodo': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Periodo',
#             }),
#             'polo': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Polo',
#             }),
#             'nome': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Nome',
#             }),
#             'telefone1': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Telefone 1',
#             }),
#             'telefone2': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Telefone 2',
#             }),
#             'email': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Email',
#             }),
#             'curso': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Curso',
#             }),
#             'status': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Status',
#             }),
#             'data_contato': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Data do contato',
#             }),
#             'observacoes': forms.Textarea(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Observacoes',
#                 'rows': 6
#             }),
#
#         }
#
#
# class ExAlunoForm(forms.ModelForm):
#     class Meta:
#         fields = [
#             'periodo',
#             'polo',
#             'curso',
#             'nome',
#             'email',
#             'telefone1',
#             'telefone2',
#             'data_contato',
#             'status',
#             'observacoes',
#         ]
#         model = ExAluno
#         # fields = ['forma_pagto', 'vendedor']
#         widgets = {
#             'periodo': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Periodo',
#             }),
#             'polo': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Polo',
#             }),
#             'nome': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Nome',
#             }),
#             'telefone1': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Telefone 1',
#             }),
#             'telefone2': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Telefone 2',
#             }),
#             'email': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Email',
#             }),
#             'curso': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Curso',
#             }),
#             'status': forms.Select(attrs={
#                 'class': 'ui fluid dropdown',
#                 'placeholder': 'Status',
#             }),
#             'data_contato': forms.TextInput(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Data do contato',
#             }),
#             'observacoes': forms.Textarea(attrs={
#                 'class': 'ui input focus',
#                 'placeholder': 'Observacoes',
#                 'rows': 6
#             }),
#
#         }
