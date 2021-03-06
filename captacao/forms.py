from django import forms
from .models import Candidato, Inscrito, ExAluno, Aluno, Periodo


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
            'periodo',
            'polo',
            'curso',
            'situacao',
            'nome',
            'email',
            'telefone1',
            'telefone2',
            'data_saida',
            'atendente',
            'status',
            'ra',
            'motivo',
            'observacoes',
        ]
        model = ExAluno
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
        #     'atendente': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Atendente',
        #     }),
        #     'status': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Status',
        #     }),
        #     'ra': forms.TextInput(attrs={
        #         'class': 'ui input focus',
        #         'placeholder': 'RA',
        #     }),
        #     'motivo': forms.Select(attrs={
        #         'class': 'ui fluid dropdown',
        #         'placeholder': 'Motivo',
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
            'nom_campus',
            'nom_curso_grupo',
            'cod_curso',
            'tipo',
            'dsc_modalidade',
            'serie',
            'semana',
            'cod_ra',
            'nom_aluno',
            'dat_matr',
            'status_aluno',
            'turma_ano_ingresso',
            'email',
            'telefone1',
            'telefone2',
            'telefone_res',
            'cidade',
            'bairro',
            'bolsista',
            'dat_ingresso',
            'data_prev_termino',
            'observacoes',
            'periodos',
        ]
        model = Aluno


class PeriodoForm(forms.ModelForm):
    fields = ['nome']
    model = Periodo
    # widgets = {
    #     'nome': forms.Select(attrs={
    #         'class': 'ui fluid dropdown',
    #         'placeholder': 'Nome',
    #     }),
    # }


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
