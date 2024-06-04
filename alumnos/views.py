from django.shortcuts import render
from .models import Genero,Alumno
# Create your views here.

def index(request):
    Alumnos = Alumno.objects.all()
    context = {"alumnos":Alumnos}
    return render(request,"alumnos/index.html",context)

def index2(request):
    Alumnos = Alumno.objects.raw('select * from alumnos_alumno')
    context = {"alumnos":Alumnos}
    return render(request,"alumnos/listadoSQL.html",context)