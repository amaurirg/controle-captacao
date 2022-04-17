from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class SituacaoInscrito(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class SituacaoExAluno(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'


class Motivo(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Motivo'
        verbose_name_plural = 'Motivos'


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


class Atendente(models.Model):
    nome = models.CharField('Nome', max_length=40)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Atendente'
        verbose_name_plural = 'Atendentes'


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
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'


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
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.CASCADE)
    data_contato = models.DateField('Data do contato')
    observacoes = models.TextField('Observacoes')
    # criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='candidato_criado_por', editable=False)
    # criado_em = models.DateTimeField(auto_now_add=True)
    # atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
    #                                    related_name='candidato_atualizado_por', editable=False, null=True, blank=True)
    # atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Candidato, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'


class Inscrito(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=40)
    telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE)
    situacao = models.ForeignKey(SituacaoInscrito, verbose_name='Situação', on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE)
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.CASCADE)
    data_contato = models.DateField('Data do contato')
    observacoes = models.TextField('Observacoes')
    # criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='inscrito_criado_por', editable=False)
    # criado_em = models.DateTimeField(auto_now_add=True)
    # atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
    #                                    related_name='inscrito_atualizado_por', editable=False, null=True, blank=True)
    # atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(Inscrito, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'


class ExAluno(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.CASCADE)
    polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=40)
    telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.CASCADE)
    situacao = models.ForeignKey(SituacaoExAluno, verbose_name='Situação', on_delete=models.CASCADE)
    data_saida = models.DateField('Data da saída')
    motivo = models.ForeignKey(Motivo, verbose_name="Motivo", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.CASCADE)
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.CASCADE)
    observacoes = models.TextField('Observacoes')
    # criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='exaluno_criado_por', editable=False)
    # criado_em = models.DateTimeField(auto_now_add=True)
    # atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
    #                                    related_name='exaluno_atualizado_por', editable=False, null=True, blank=True)
    # atualizado_em = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(ExAluno, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Ex Aluno'
        verbose_name_plural = 'Ex Alunos'