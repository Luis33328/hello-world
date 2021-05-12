from django.shortcuts import render, get_object_or_404, redirect
from .models import Disciplina, Matricula
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'gestaoacademicaapp/login.html')

def esq(request):
    return render(request, 'gestaoacademicaapp/esq_senha.html')

@login_required
def home(request):
    return render(request, 'gestaoacademicaapp/home.html')

@login_required
def listaMatriculas(request):

    #listadisciplina = Matricula.objects.all
    listadisciplina = Matricula.objects.filter(estudante=request.user)


    return render(request, 'gestaoacademicaapp/index.html', {'disciplinas':listadisciplina})

@login_required
def fazerMatricula(request, id):

    matriculardisciplina = get_object_or_404(Matricula, pk = id)

    if(matriculardisciplina.status == 'prevista'):
        matriculardisciplina.status = 'matriculado'

    matriculardisciplina.save()

    return redirect('/')
