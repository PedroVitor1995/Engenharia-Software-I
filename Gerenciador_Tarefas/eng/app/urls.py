from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('importar/', views.importar_alunos, name='importar_alunos'),
	path('alunos/', views.listar_alunos, name='listar_alunos'),
	path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
	path('tarefas', views.listar_tarefas, name='listar_tarefas'),
	path('criar_grupo/', views.criar_grupo, name='criar_grupo'),
	path('grupos/', views.listar_grupos, name='listar_grupos'),
	path('sortear/tarefa/<int:tarefa_id>/', views.sortear, name='sortear'),
	path('grupo/aluno/<int:aluno_id>/', views.grupo_aluno, name='grupo_aluno')
]
