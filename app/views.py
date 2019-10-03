from django.shortcuts import render,redirect

# Create your views here.

from .models import *

def index(request):	
	return render(request,'home.html')

def import_csv(request):
	arquivo = request.FILES["file_csv"]
	lista = ""
	lista = arquivo.read().decode('iso-8859-1')
	alunos = lista.replace("\r","").split("\n")
	for aluno in alunos:
		if(len(aluno) > 0):
			Aluno.objects.create(nome = aluno)
	
	alunos = Aluno.objects.all()
	return render(request,'lista_alunos.html',{"alunos":alunos})

def listar_alunos(request):
	alunos = Aluno.objects.all()
	return render(request,'lista_alunos.html',{'alunos':alunos})

