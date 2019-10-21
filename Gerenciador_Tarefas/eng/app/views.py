from django.shortcuts import render,redirect

# Create your views here.

from .models import *
from .forms import *
import random

def index(request):	
	return render(request,'home.html')

def importar_alunos(request):
	if request.POST:
		form = AlunoForm(request.POST)
		if form.is_valid():
			arquivo = request.FILES["file"]
			lista = ""
			lista = arquivo.read().decode('iso-8859-1')
			alunos = lista.replace("\r","").split("\n")
			for aluno in alunos:
				if(len(aluno) > 0):
					Aluno.objects.create(nome = aluno)
			return redirect('listar_alunos')

	return render(request,'importa.html')

def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request,'lista_alunos.html',{'alunos':alunos})

def listar_tarefas(request):
	tarefas = Tarefa.objects.all()
	return render(request,'lista_tarefas.html',{'tarefas':tarefas})

def criar_tarefa(request):
	if request.POST:
		form = TarefaForm(request.POST)
		if form.is_valid():
			descricao = request.POST['descricao']
			data = request.POST['data']
			Tarefa.objects.create(descricao = descricao, data_realizacao = data)
			return redirect('listar_tarefas')

	return render(request,'cria_tarefa.html')

def listar_grupos(request):
	grupos = Grupo.objects.all()
	return render(request,'lista_grupos.html',{'grupos':grupos})

def criar_grupo(request):
	if request.POST:
		form = GrupoForm(request.POST)
		if form.is_valid():
			descricao = request.POST['descricao']
			Grupo.objects.create(descricao = descricao)
			return redirect('listar_grupos')
	return render(request,'cria_grupo.html')

def sortear(request,tarefa_id):
	tarefa = Tarefa.objects.get(id=tarefa_id)
	if request.POST:
		tipo = request.POST['type']
		if tipo == 'aluno':
			aluno = random.choice(list(Aluno.objects.all()))
			tarefa.aluno = aluno
			tarefa.save()
			return redirect('listar_tarefas')
		if tipo == 'grupo':
			grupo = random.choice(list(Grupo.objects.all()))
			tarefa.grupo = grupo
			tarefa.save()
			return redirect('listar_tarefas')
	return render(request,'sorteio.html',{'tarefa': tarefa})

def grupo_aluno(request,aluno_id):
	aluno = Aluno.objects.get(id=aluno_id)
	grupos = Grupo.objects.all()
	if request.POST:
		grupo_id = request.POST['group']
		grupo = Grupo.objects.get(id=grupo_id)
		aluno.grupo = grupo
		aluno.save()
		return redirect('listar_alunos')
	return render(request,'grupo_aluno.html',{'aluno': aluno, 'grupos': grupos})

