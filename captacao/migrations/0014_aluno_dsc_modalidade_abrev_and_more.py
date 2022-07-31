# Generated by Django 4.0.3 on 2022-06-24 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('captacao', '0013_modalidade_curso_nome_abrev_polo_nome_abrev'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='dsc_modalidade_abrev',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='captacao.modalidade', verbose_name='DscModalidadeAbrev'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nom_campus_abrev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.polo', verbose_name='NomCampusAbrev'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='nom_curso_grupo_abrev',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='captacao.curso', verbose_name='NomCursoGrupoAbrev'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nome_abrev',
            field=models.CharField(max_length=50, verbose_name='NomeAbrev'),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='modalidade',
            name='nome_abrev',
            field=models.CharField(max_length=50, verbose_name='NomeAbrev'),
        ),
        migrations.AlterField(
            model_name='periodo',
            name='nome',
            field=models.CharField(max_length=10, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='polo',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='polo',
            name='nome_abrev',
            field=models.CharField(max_length=50, verbose_name='NomeAbrev'),
        ),
    ]