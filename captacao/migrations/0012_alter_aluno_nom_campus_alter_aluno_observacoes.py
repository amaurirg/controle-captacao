# Generated by Django 4.0.3 on 2022-06-24 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('captacao', '0011_alter_aluno_nom_campus_abrev_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='nom_campus',
            field=models.CharField(max_length=150, verbose_name='NomCampus'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='observacoes',
            field=models.TextField(blank=True, null=True, verbose_name='Observacoes'),
        ),
    ]
