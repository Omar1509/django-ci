from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'Academico/lista_cursos.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'Academico/crear_curso.html', {'form': form})
