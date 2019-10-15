from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=300)

	def __str__(self):
		return self.nome

class Tarefa(models.Model):
	descricao = models.CharField(max_length=300)
	data_realizacao = models.DateField()
	aluno = models.ForeignKey(Aluno, related_name='alunos',on_delete="CASCADE")