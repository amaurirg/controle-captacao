from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class Marketing(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Marketing'
        verbose_name_plural = 'Marketing'


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


# class Atendente(models.Model):
#     nome = models.CharField('Nome', max_length=40)
#
#     def __str__(self):
#         return self.nome
#
#     class Meta:
#         verbose_name = 'Atendente'
#         verbose_name_plural = 'Atendentes'


class Polo(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Polo'
        verbose_name_plural = 'Polos'


class Periodo(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Periodo'
        verbose_name_plural = 'Periodos'


class Candidato(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=40)
    telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE)
    marketing = models.ForeignKey(Marketing, verbose_name='Marketing', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE)
    atendente = models.ForeignKey(User, verbose_name='Atendente', on_delete=models.PROTECT, related_name='atendente', editable=False)
    data_contato = models.DateField('Data do contato')
    observacoes = models.TextField('Observacoes')

    def save(self, *args, **kwargs):
        super(Candidato, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
