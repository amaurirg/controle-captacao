# Generated by Django 4.0.3 on 2022-08-06 00:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('captacao', '0002_candidato_atendimentos_atendimentosaluno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimentosaluno',
            name='candidato',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='atendimentos_aluno', to='captacao.candidato'),
        ),
    ]
