from django.urls import path
from app import views

urlpatterns = [
	path('', views.index, name='index'),
	path('importar/', views.import_csv, name='import_csv'),
	path('lista/', views.listar_alunos, name='listar_alunos'),
]
