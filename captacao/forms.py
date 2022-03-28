from django import forms
from .models import Candidato


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
            'observacoes',
        ]
        model = Candidato
        # fields = ['forma_pagto', 'vendedor']
        widgets = {
            'periodo': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Periodo',
            }),
            'polo': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Polo',
            }),
            'nome': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Nome',
            }),
            'telefone1': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Telefone 1',
            }),
            'telefone2': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Telefone 2',
            }),
            'email': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Email',
            }),
            'curso': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Curso',
            }),
            'marketing': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Marketing',
            }),
            'status': forms.Select(attrs={
                'class': 'ui fluid dropdown',
                'placeholder': 'Status',
            }),
            'data_contato': forms.TextInput(attrs={
                'class': 'ui input focus',
                'placeholder': 'Data do contato',
            }),
            'observacoes': forms.Textarea(attrs={
                'class': 'ui input focus',
                'placeholder': 'Observacoes',
                'rows': 6
            }),

        }
