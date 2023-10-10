from django.urls import path

from cadastro import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('listar_professor', views.listarProfessores),
    path('listar_aluno', views.listarAlunos)


]
