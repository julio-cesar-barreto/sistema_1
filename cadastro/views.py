from django.http import HttpResponse
from django.shortcuts import render

from cadastro.models import Professor, Aluno


# Create your views here.

def index(request):
    return HttpResponse("Olá, Mundo ! Agora estou na Web")

def listarProfessores(request):
    professores = Professor.objects.all().order_by('nome')
    return render(request, "listar_professor.html", {'lista':professores})

def listarAlunos(request):
    alunos = Aluno.objects.all().order_by('nome')
    return render(request, "listar_aluno.html", {'lista':alunos})
