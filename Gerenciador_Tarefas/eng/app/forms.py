from django import forms
from .models import *


class AlunoForm(forms.Form):
	class Meta:
		model = Aluno
		fields = '__all__'

class GrupoForm(forms.Form):
	class Meta:
		model = Grupo
		fields = '__all__'

class TarefaForm(forms.Form):
	class Meta:
		model = Tarefa
		fields = '__all__'