from django.db import models

# Create your models here.

class Aluno(models.Model):
	nome = models.CharField(max_length=300)
	grupo = models.ForeignKey("Grupo", related_name='grupo',on_delete="CASCADE", null = True)

	def __str__(self):
		return self.nome
		
class Grupo(models.Model):
	descricao = models.CharField(max_length=300)

class Tarefa(models.Model):
	descricao = models.CharField(max_length=300)
	data_realizacao = models.DateField()
	aluno = models.ForeignKey(Aluno, on_delete="CASCADE", null = True)
	grupo = models.ForeignKey(Grupo, on_delete="CASCADE", null = True)

