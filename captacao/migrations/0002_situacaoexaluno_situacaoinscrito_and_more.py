# Generated by Django 4.0.3 on 2022-04-16 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('captacao', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SituacaoExAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Situação',
                'verbose_name_plural': 'Situações',
            },
        ),
        migrations.CreateModel(
            name='SituacaoInscrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Situação',
                'verbose_name_plural': 'Situações',
            },
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='atualizado_em',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='atualizado_por',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='criado_em',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='situacao',
        ),
        migrations.RemoveField(
            model_name='exaluno',
            name='atualizado_em',
        ),
        migrations.RemoveField(
            model_name='exaluno',
            name='atualizado_por',
        ),
        migrations.RemoveField(
            model_name='exaluno',
            name='criado_em',
        ),
        migrations.RemoveField(
            model_name='exaluno',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='inscrito',
            name='atualizado_em',
        ),
        migrations.RemoveField(
            model_name='inscrito',
            name='atualizado_por',
        ),
        migrations.RemoveField(
            model_name='inscrito',
            name='criado_em',
        ),
        migrations.RemoveField(
            model_name='inscrito',
            name='criado_por',
        ),
        migrations.AlterField(
            model_name='exaluno',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captacao.situacaoexaluno', verbose_name='Situação'),
        ),
        migrations.AlterField(
            model_name='inscrito',
            name='situacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captacao.situacaoinscrito', verbose_name='Situação'),
        ),
        migrations.DeleteModel(
            name='Situacao',
        ),
    ]
