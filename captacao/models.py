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


class Candidato(models.Model):
    polo = models.ForeignKey(Polo, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=40)
    telefone1 = models.CharField('Telefone 1', max_length=20)
    telefone2 = models.CharField('Telefone 2', max_length=20)
    email = models.EmailField('Email', max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    marketing = models.ForeignKey(Marketing, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE)
    data_contato = models.DateTimeField()
    observacoes = models.TextField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Candidato'
        verbose_name_plural = 'Candidatos'
