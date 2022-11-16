from django import forms
from .models import Candidato, Inscrito, Aluno, ExAluno, AtendimentosCandidato, AtendimentosInscrito, \
    AtendimentosExAluno, AtendimentosAluno


class CandidatoForm(forms.ModelForm):
    class Meta:
        fields = [
            'polo',
            'curso',
            'marketing',
            'nome',
            'email',
            'telefone1',
            'telefone2',
            'status_atendimento',
            'periodos',
            'observacoes',
        ]
        model = Candidato

        widgets = {
            'status_atendimento': forms.TextInput(
                attrs={
                    'readonly': 'readonly',
                    'id': 'ultimo-status'
                }
            ),
        }


class InscritoForm(forms.ModelForm):
    class Meta:
        fields = [
            'polo',
            'curso',
            'situacao',
            'nome',
            'email',
            'telefone1',
            'telefone2',
            'status_atendimento',
            'periodos',
            'observacoes',
        ]
        model = Inscrito


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
            # 'data_saida': forms.TextInput(attrs={'readonly': 'readonly'}),
            'periodos': forms.SelectMultiple(attrs={'readonly': 'readonly'})
        }


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


class AtendimentosCandidatoForm(forms.ModelForm):
    class Meta:
        fields = ['descricao', 'status']
        model = AtendimentosCandidato


class AtendimentosInscritoForm(forms.ModelForm):
    class Meta:
        fields = ['descricao', 'status']
        model = AtendimentosInscrito


class AtendimentosExAlunoForm(forms.ModelForm):
    class Meta:
        fields = ['descricao', 'status']
        model = AtendimentosExAluno


class AtendimentosAlunoForm(forms.ModelForm):
    class Meta:
        fields = ['descricao', 'status']
        model = AtendimentosAluno
