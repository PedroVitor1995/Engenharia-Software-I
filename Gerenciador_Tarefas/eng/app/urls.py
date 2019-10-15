from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('importar/', views.importar, name='importar'),
	path('importado/', views.importar_alunos, name='importar_alunos'),
	path('alunos/', views.listar_alunos, name='listar_alunos'),
	path('tarefas', views.listar_tarefas, name='listar_tarefas'),
]
