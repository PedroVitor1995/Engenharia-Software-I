from django.shortcuts import render,redirect

# Create your views here.

from .models import *

def index(request):	
	return render(request,'home.html')

def importar(request):
	return render(request,'importar.html')

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

def cria_tarefa(request):
	if request.POST:
		form = Tarefa(request.POST)
		if form.is_valid():
			descricao = request.POST['descricao']
			data_realizacao = request.POST['data_realizacao']
			Tarefa.objects.create(descricao = texto, )
			messages.success(request, 'Postagem feita com sucesso.')
		else:
			messages.error(request, 'Não foi possivel fazer a postagem')

	return redirect('timeline')

