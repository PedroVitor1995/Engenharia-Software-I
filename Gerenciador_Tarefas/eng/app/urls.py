from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('importar/', views.importar, name='importar'),
	path('importado/', views.importar_alunos, name='importar_alunos'),
	path('alunos/', views.listar_alunos, name='listar_alunos'),
	path('criar_tarefa/', views.criar_tarefa, name='criar_tarefa'),
	path('tarefas', views.listar_tarefas, name='listar_tarefas'),
	path('criar_grupo/', views.criar_grupo, name='criar_grupo'),
	path('grupos', views.listar_grupos, name='listar_grupos'),
]
