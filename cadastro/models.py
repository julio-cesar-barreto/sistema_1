from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(max_length = 20, null = False)
    email = models.CharField(max_length = 20, null = False)
    telefone = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.nome
class Aluno(models.Model):
    nome = models.CharField(max_length=20, null=False)
    dataNascimento = models.DateField(max_length=10, null=False)
    endereco = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=20, null=False)
    telefone = models.CharField(max_length=15, null=False)

    def __str__(self):
        return self.nome