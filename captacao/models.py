from django.contrib.auth.models import User
from django.db import models


class Status(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Status'
        verbose_name_plural = 'Status'


class SituacaoInscrito(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Situação Inscrito'
        verbose_name_plural = 'Situação Inscritos'


class SituacaoExAluno(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Situação ExAluno'
        verbose_name_plural = 'Situação ExAlunos'


class Motivo(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Motivo'
        verbose_name_plural = 'Motivos'


class Marketing(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Marketing'
        verbose_name_plural = 'Marketing'


class Curso(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    nome_abrev = models.CharField('NomeAbrev', max_length=50, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_abrev

    class Meta:
        ordering = ['nome_abrev']
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Atendente(models.Model):
    nome = models.CharField('Nome', max_length=40, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Atendente'
        verbose_name_plural = 'Atendentes'


class Polo(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    nome_abrev = models.CharField('NomeAbrev', max_length=50, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_abrev

    class Meta:
        ordering = ['nome_abrev']
        verbose_name = 'Polo'
        verbose_name_plural = 'Polos'


class Periodo(models.Model):
    nome = models.CharField('Nome', max_length=10, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'


class Modalidade(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    nome_abrev = models.CharField('NomeAbrev', max_length=50, unique=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_abrev

    class Meta:
        ordering = ['nome']
        verbose_name = 'Modalidade'
        verbose_name_plural = 'Modalidades'


class Candidato(models.Model):
    polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=40, unique=True)
    telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.PROTECT)
    marketing = models.ForeignKey(Marketing, verbose_name='Marketing', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.PROTECT)
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.PROTECT)
    data_contato = models.DateField('Data do contato')
    observacoes = models.TextField('Observações', null=True, blank=True)
    ativo = models.BooleanField(default=True)
    periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.PROTECT)
    atendimentos = models.TextField('Atendimentos', null=True, blank=True)
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
        ordering = ['nome']
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'


class Inscrito(models.Model):
    periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.PROTECT)
    polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.PROTECT)
    nome = models.CharField('Nome', max_length=40, unique=True)
    telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
    telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, null=True, blank=True)
    curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.PROTECT)
    situacao = models.ForeignKey(SituacaoInscrito, verbose_name='Situação', on_delete=models.PROTECT)
    status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.PROTECT)
    atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.PROTECT)
    data_contato = models.DateField('Data do contato')
    observacoes = models.TextField('Observacoes', null=True, blank=True)
    ativo = models.BooleanField(default=True)

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
        ordering = ['nome']
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'


# class ExAluno(models.Model):
# periodo = models.ForeignKey(Periodo, verbose_name='Período', on_delete=models.PROTECT)
# polo = models.ForeignKey(Polo, verbose_name='Polo', on_delete=models.PROTECT)
# ra = models.CharField('RA', max_length=7)
# nome = models.CharField('Nome', max_length=40, unique=True)
# telefone1 = models.CharField('Telefone 1', max_length=20, null=True, blank=True)
# telefone2 = models.CharField('Telefone 2', max_length=20, null=True, blank=True)
# email = models.EmailField('Email', max_length=100, null=True, blank=True)
# curso = models.ForeignKey(Curso, verbose_name='Curso', on_delete=models.PROTECT)
# situacao = models.ForeignKey(SituacaoExAluno, verbose_name='Situação', on_delete=models.PROTECT)
# data_saida = models.DateField('Data da saída')
# motivo = models.ForeignKey(Motivo, verbose_name="Motivo", on_delete=models.PROTECT)
# status = models.ForeignKey(Status, verbose_name='Status', on_delete=models.PROTECT)
# atendente = models.ForeignKey(Atendente, verbose_name='Atendente', on_delete=models.PROTECT)
# observacoes = models.TextField('Observacoes', null=True, blank=True)
# ativo = models.BooleanField(default=True)


class ExAluno(models.Model):
    nom_campus = models.ForeignKey(Polo, verbose_name='NomCampus', on_delete=models.PROTECT)
    nom_aluno = models.CharField('NomAluno', max_length=255)
    cod_ra = models.PositiveIntegerField('CodRA')
    dsc_modalidade = models.ForeignKey(Modalidade, verbose_name='DscModalidade', on_delete=models.PROTECT)
    nom_curso_grupo = models.ForeignKey(Curso, verbose_name='NomCursoGrupo', on_delete=models.PROTECT)
    # situacao = models.ForeignKey(SituacaoExAluno, verbose_name='Situacao', on_delete=models.PROTECT)
    data_saida = models.DateField('DataSaida', blank=True, null=True)
    dsc_status_matr = models.CharField('DscStatusMatr', max_length=255)
    turma_ano_ingresso = models.CharField('TurmaAnoIngresso', max_length=50)
    turma_ano_ingresso_abrev = models.CharField('TurmaAnoIngressoAbrev', max_length=20, editable=False)
    email = models.EmailField('Email', max_length=255, blank=True, null=True)
    telefone1 = models.CharField('TelefoneCel1', max_length=15, blank=True, null=True)
    telefone2 = models.CharField('TelefoneCel2', max_length=15, blank=True, null=True)
    telefone_res = models.CharField('TelefoneRes', max_length=15, blank=True, null=True)
    observacoes = models.TextField('Observacoes', null=True, blank=True)
    periodos = models.ManyToManyField(Periodo, verbose_name='Períodos', related_name='periodos_exaluno', blank=True)
    ativo = models.BooleanField(default=True)

    # criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='exaluno_criado_por', editable=False)
    # criado_em = models.DateTimeField(auto_now_add=True)
    # atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
    #                                    related_name='exaluno_atualizado_por', editable=False, null=True, blank=True)
    # atualizado_em = models.DateTimeField(auto_now=True)

    # def save(self, *args, **kwargs):
    #     super(ExAluno, self).save(*args, **kwargs)

    def __str__(self):
        return self.nom_aluno

    class Meta:
        ordering = ['nom_aluno']
        verbose_name = 'Ex Aluno'
        verbose_name_plural = 'Ex Alunos'


class Aluno(models.Model):
    nom_campus = models.ForeignKey(Polo, verbose_name='NomCampus', on_delete=models.PROTECT)
    nom_curso_grupo = models.ForeignKey(Curso, verbose_name='NomCursoGrupo', on_delete=models.PROTECT)
    cod_curso = models.PositiveIntegerField('CodCurso')
    tipo = models.CharField('Tipo', max_length=20)
    dsc_modalidade = models.ForeignKey(Modalidade, verbose_name='DscModalidade', on_delete=models.PROTECT)
    serie = models.PositiveSmallIntegerField('Serie')
    semana = models.CharField('Semana', max_length=15)
    cod_ra = models.PositiveIntegerField('CodRA')
    nom_aluno = models.CharField('NomAluno', max_length=255)
    dat_matr = models.DateField('DatMatr')
    status_aluno = models.CharField('StatusAluno', max_length=30)
    turma_ano_ingresso = models.CharField('TurmaAnoIngresso', max_length=50)
    turma_ano_ingresso_abrev = models.CharField('TurmaAnoIngressoAbrev', max_length=20, editable=False)
    email = models.EmailField('Email', max_length=255, blank=True, null=True)
    telefone1 = models.CharField('TelefoneCel1', max_length=15, blank=True, null=True)
    telefone2 = models.CharField('TelefoneCel2', max_length=15, blank=True, null=True)
    telefone_res = models.CharField('TelefoneRes', max_length=15, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=255)
    bairro = models.CharField('Bairro', max_length=255)
    bolsista = models.CharField('Bolsista', max_length=5)
    dat_ingresso = models.DateField('Dat_ingresso')
    data_prev_termino = models.DateField('DataPrevTermino')
    observacoes = models.TextField('Observacoes', null=True, blank=True)
    periodos = models.ManyToManyField(Periodo, verbose_name='Períodos', related_name='periodos_aluno', blank=True)
    ativo = models.BooleanField(default=True)

    # criado_por = models.ForeignKey(User, on_delete=models.PROTECT, related_name='exaluno_criado_por', editable=False)
    # criado_em = models.DateTimeField(auto_now_add=True)
    # atualizado_por = models.ForeignKey(User, on_delete=models.PROTECT,
    #                                    related_name='exaluno_atualizado_por', editable=False, null=True, blank=True)
    # atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom_aluno

    class Meta:
        ordering = ['nom_aluno']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


class AtendimentosAluno(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField('Descrição')
    candidato = models.ForeignKey(Candidato, on_delete=models.PROTECT, related_name='atendimentos_aluno')

    def __str__(self):
        return str(self.data)

    class Meta:
        ordering = ['-data']
        verbose_name = 'Atendimentos dos Aluno'
        verbose_name_plural = 'Atendimentos dos Alunos'
