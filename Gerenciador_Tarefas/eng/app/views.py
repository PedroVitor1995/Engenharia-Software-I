from django.shortcuts import render,redirect

# Create your views here.

from .models import *

def index(request):	
	return render(request,'home.html')

def importar(request):
	return render(request,'importa.html')

def importar_alunos(request):
	arquivo = request.FILES["file"]
	lista = ""
	lista = arquivo.read().decode('iso-8859-1')
	alunos = lista.replace("\r","").split("\n")
	for aluno in alunos:
		if(len(aluno) > 0):
			Aluno.objects.create(nome = aluno)
	return redirect('importar')

def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request,'lista_alunos.html',{'alunos':alunos})

def listar_tarefas(request):
	tarefas = Tarefa.objects.all()
	return render(request,'lista_tarefas.html',{'tarefas':tarefas})

def criar_tarefa(request):
	return render(request,'cria_tarefa.html')

def listar_grupos(request):
	grupos = Grupo.objects.all()
	return render(request,'lista_grupos.html',{'grupos':grupos})

def criar_grupo(request):
	return render(request,'cria_grupo.html')


