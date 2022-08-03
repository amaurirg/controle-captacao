from django import forms
from .models import Candidato, Inscrito, Aluno, ExAluno


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

        # widgets = {
        #     'periodo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Período',
        #     }),
        #     'polo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Polo',
        #     }),
        #     'curso': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Curso',
        #     }),
        #     'marketing': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Marketing',
        #     }),
        #     'nome': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Nome',
        #     }),
        #     'email': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Email',
        #     }),
        #     'telefone1': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 1',
        #     }),
        #     'telefone2': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 2',
        #     }),
        #     'data_contato': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Data do contato',
        #     }),
        #     'status': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Status',
        #     }),
        #     'atendente': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Atendente',
        #     }),
        #     'observacoes': forms.Textarea(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Observações',
        #         'rows': 6
        #     }),
        #
        # }


class InscritoForm(forms.ModelForm):
    class Meta:
        fields = [
            'periodo',
            'polo',
            'curso',
            'situacao',
            'nome',
            'email',
            'telefone1',
            'telefone2',
            'data_contato',
            'status',
            'atendente',
            'observacoes',
        ]
        model = Inscrito

        # widgets = {
        #     'periodo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Período',
        #     }),
        #     'polo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Polo',
        #     }),
        #     'curso': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Curso',
        #     }),
        #     'situacao': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Situacao',
        #     }),
        #     'nome': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Nome',
        #     }),
        #     'email': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Email',
        #     }),
        #     'telefone1': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 1',
        #     }),
        #     'telefone2': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 2',
        #     }),
        #     'data_contato': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Data do contato',
        #     }),
        #     'status': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Status',
        #     }),
        #     'atendente': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Atendente',
        #     }),
        #     'observacoes': forms.Textarea(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Observações',
        #         'rows': 6
        #     }),
        #
        # }


class ExAlunoForm(forms.ModelForm):
    class Meta:
        fields = [
            'nom_aluno',
            'email',
            'telefone1',
            'telefone2',
            'telefone_res',
            'cod_ra',
            'data_saida',
            'periodos',
            'observacoes',
        ]

        model = ExAluno
        widgets = {
            'nom_aluno': forms.TextInput(attrs={'readonly': 'readonly'}),
            'cod_ra': forms.TextInput(attrs={'readonly': 'readonly'}),
            'data_saida': forms.TextInput(attrs={'readonly': 'readonly'}),
            'periodos': forms.SelectMultiple(attrs={'readonly': 'readonly'})
        }

        # widgets = {
        #     'periodo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Período',
        #     }),
        #     'polo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Polo',
        #     }),
        #     'curso': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Curso',
        #     }),
        #     'situacao': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Situacao',
        #     }),
        #     'nome': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Nome',
        #     }),
        #     'email': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Email',
        #     }),
        #     'telefone1': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 1',
        #     }),
        #     'telefone2': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Telefone 2',
        #     }),
        #     'data_saida': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Data do contato',
        #     }),
        #     'status': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Status',
        #     }),
        #     'ra': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'RA',
        #     }),
        #     'observacoes': forms.Textarea(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'Observações',
        #         'rows': 6
        #     }),
        #
        # }


class AlunoForm(forms.ModelForm):
    class Meta:
        fields = [
            'nom_aluno',
            'email',
            'telefone1',
            'telefone2',
            'telefone_res',
            'cod_ra',
            'cidade',
            'bairro',
            'periodos',
            'observacoes',
        ]
        model = Aluno
        widgets = {
            'nom_aluno': forms.TextInput(attrs={'readonly': 'readonly'}),
            'cod_ra': forms.TextInput(attrs={'readonly': 'readonly'}),
            'periodos': forms.SelectMultiple(attrs={'readonly': 'readonly'})
        }


class CreateNewForm(forms.Form):
    name = forms.CharField(max_length=50)
    widgets = {
        'name': forms.TextInput(
            attrs={
                'class': 'ui input focus',
                'placeholder': 'Digite um novo',
            }
        )
    }
