from django.urls import path
from app import views

urlpatterns = [
	path('', views.index, name='index'),
	path('listar/', views.import_csv, name='import_csv'),
]
