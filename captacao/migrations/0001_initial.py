# Generated by Django 4.0.3 on 2022-08-15 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_curso', models.PositiveIntegerField(verbose_name='CodCurso')),
                ('tipo', models.CharField(max_length=20, verbose_name='Tipo')),
                ('serie', models.PositiveSmallIntegerField(verbose_name='Serie')),
                ('semana', models.CharField(max_length=15, verbose_name='Semana')),
                ('cod_ra', models.PositiveIntegerField(verbose_name='CodRA')),
                ('nom_aluno', models.CharField(max_length=255, verbose_name='NomAluno')),
                ('dat_matr', models.DateField(verbose_name='DatMatr')),
                ('status_aluno', models.CharField(max_length=30, verbose_name='StatusAluno')),
                ('turma_ano_ingresso', models.CharField(max_length=50, verbose_name='TurmaAnoIngresso')),
                ('turma_ano_ingresso_abrev', models.CharField(editable=False, max_length=20, verbose_name='TurmaAnoIngressoAbrev')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('telefone1', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneCel1')),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneCel2')),
                ('telefone_res', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneRes')),
                ('cidade', models.CharField(max_length=255, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=255, verbose_name='Bairro')),
                ('bolsista', models.CharField(max_length=5, verbose_name='Bolsista')),
                ('dat_ingresso', models.DateField(verbose_name='Dat_ingresso')),
                ('data_prev_termino', models.DateField(verbose_name='DataPrevTermino')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='aluno_atualizado_por', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='aluno_criado_por', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Aluno',
                'verbose_name_plural': 'Alunos',
                'ordering': ['nom_aluno'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('nome_abrev', models.CharField(max_length=50, unique=True, verbose_name='NomeAbrev')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['nome_abrev'],
            },
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Marketing',
                'verbose_name_plural': 'Marketing',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('nome_abrev', models.CharField(max_length=50, unique=True, verbose_name='NomeAbrev')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Modalidade',
                'verbose_name_plural': 'Modalidades',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Motivo',
                'verbose_name_plural': 'Motivos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Polo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True, verbose_name='Nome')),
                ('nome_abrev', models.CharField(max_length=50, unique=True, verbose_name='NomeAbrev')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Polo',
                'verbose_name_plural': 'Polos',
                'ordering': ['nome_abrev'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoExAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Situação ExAluno',
                'verbose_name_plural': 'Situação ExAlunos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='SituacaoInscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Situação Inscrito',
                'verbose_name_plural': 'Situação Inscritos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='StatusAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('telefone1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 2')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('data_contato', models.DateField(verbose_name='Data do contato')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='inscrito_atualizado_por', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='inscrito_criado_por', to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.curso', verbose_name='Curso')),
                ('periodos', models.ManyToManyField(blank=True, related_name='periodos_inscrito', to='captacao.periodo', verbose_name='Períodos')),
                ('polo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.polo', verbose_name='Polo')),
                ('situacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.situacaoinscrito', verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Inscrito',
                'verbose_name_plural': 'Inscritos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='ExAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_aluno', models.CharField(max_length=255, verbose_name='NomAluno')),
                ('cod_ra', models.PositiveIntegerField(verbose_name='CodRA')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='DataSaida')),
                ('dsc_status_matr', models.CharField(max_length=255, verbose_name='DscStatusMatr')),
                ('turma_ano_ingresso', models.CharField(max_length=50, verbose_name='TurmaAnoIngresso')),
                ('turma_ano_ingresso_abrev', models.CharField(editable=False, max_length=20, verbose_name='TurmaAnoIngressoAbrev')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email')),
                ('telefone1', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneCel1')),
                ('telefone2', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneCel2')),
                ('telefone_res', models.CharField(blank=True, max_length=15, null=True, verbose_name='TelefoneRes')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observacoes')),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exaluno_atualizado_por', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='exaluno_criado_por', to=settings.AUTH_USER_MODEL)),
                ('dsc_modalidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.modalidade', verbose_name='DscModalidade')),
                ('nom_campus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.polo', verbose_name='NomCampus')),
                ('nom_curso_grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.curso', verbose_name='NomCursoGrupo')),
                ('periodos', models.ManyToManyField(blank=True, related_name='periodos_exaluno', to='captacao.periodo', verbose_name='Períodos')),
            ],
            options={
                'verbose_name': 'Ex Aluno',
                'verbose_name_plural': 'Ex Alunos',
                'ordering': ['nom_aluno'],
            },
        ),
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, unique=True, verbose_name='Nome')),
                ('telefone1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 1')),
                ('telefone2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefone 2')),
                ('email', models.EmailField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('data_contato', models.DateField(verbose_name='Data do contato')),
                ('observacoes', models.TextField(blank=True, null=True, verbose_name='Observações')),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('atualizado_por', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='candidato_atualizado_por', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='candidato_criado_por', to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.curso', verbose_name='Curso')),
                ('marketing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.marketing', verbose_name='Marketing')),
                ('periodos', models.ManyToManyField(blank=True, related_name='periodos_candidato', to='captacao.periodo', verbose_name='Períodos')),
                ('polo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.polo', verbose_name='Polo')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='AtendimentosInscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('atendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='atendente_inscrito', to=settings.AUTH_USER_MODEL)),
                ('inscrito', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimentos_inscrito', to='captacao.inscrito')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.statusatendimento', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Atendimentos do Inscrito',
                'verbose_name_plural': 'Atendimentos dos Inscritos',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='AtendimentosExAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('atendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='atendente_exaluno', to=settings.AUTH_USER_MODEL)),
                ('exaluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimentos_exaluno', to='captacao.exaluno')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.statusatendimento', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Atendimentos do Ex-Aluno',
                'verbose_name_plural': 'Atendimentos dos Ex-Alunos',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='AtendimentosCandidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('atendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='atendente_candidato', to=settings.AUTH_USER_MODEL)),
                ('candidato', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimentos_candidato', to='captacao.candidato')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.statusatendimento', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Atendimentos do Candidato',
                'verbose_name_plural': 'Atendimentos dos Candidatos',
                'ordering': ['-data'],
            },
        ),
        migrations.CreateModel(
            name='AtendimentosAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimentos_aluno', to='captacao.aluno')),
                ('atendente', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='atendente_aluno', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.statusatendimento', verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Atendimentos do Aluno',
                'verbose_name_plural': 'Atendimentos dos Alunos',
                'ordering': ['-data'],
            },
        ),
        migrations.AddField(
            model_name='aluno',
            name='dsc_modalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.modalidade', verbose_name='DscModalidade'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='nom_campus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.polo', verbose_name='NomCampus'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='nom_curso_grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.curso', verbose_name='NomCursoGrupo'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='periodos',
            field=models.ManyToManyField(blank=True, related_name='periodos_aluno', to='captacao.periodo', verbose_name='Períodos'),
        ),
    ]
