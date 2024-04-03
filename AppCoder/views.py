from django.shortcuts import render, redirect 
from AppCoder.models import Curso, Usuario, Alumnos, Profesores
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout #pendiente hacer el logout
from django.contrib.auth.hashers import make_password


#Alumnos
   
def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    dicc = {"alumnos": alumnos}
    plantilla = loader.get_template("ver_alumnos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def alumno_formulario(request):
    if request.method == "POST":
        el_formulario = Alumnos_formulario(request.POST)
        if el_formulario.is_valid():
            datos = el_formulario.cleaned_data
            alumno = Alumnos(nombre=datos["nombre"], edad=datos["edad"], email=datos["email"])
            alumno.save()
            return redirect('ver_alumnos')  
   
    return render(request, "alta_alumnos.html")

#Profesores

def ver_profesores(request):
    profesores = Profesores.objects.all()
    dicc = {"profesores": profesores}
    plantilla = loader.get_template("ver_profesores.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def profesor_formulario(request):
    if request.method == "POST":
        su_formulario = Profesores_formulario(request.POST)
        if su_formulario.is_valid():
            datos = su_formulario.cleaned_data
            profesor = Profesores(nombre=datos["nombre"], asignatura=datos["asignatura"], email=datos["email"])
            profesor.save()
            return redirect('ver_profesores')  
   

    return render(request, "alta_profesores.html")

#Inicio
def inicio(request):
    return render(request, "padre.html")


#Cursos

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos = Curso.objects.all()
    dicc = {"cursos": cursos}
    plantilla = loader.get_template("cursos.html")
    documento = plantilla.render(dicc)
    return HttpResponse(documento)

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = Curso_formulario(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso =Curso(nombre=datos["nombre"], camada=datos["camada"])
            curso.save()
            return render(request , "formulario.html")

    return render(request , "formulario.html")


def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):    
    if  request.GET["nombre"]:
        nombre = request.GET["nombre"]
        cursos = Curso.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html" , {"cursos":cursos})
    else:
        return HttpResponse("Ingrese el nombre del curso")   
    
    
def elimina_curso(request , id):
    curso = Curso.objects.get(id=id).delete()     

    curso = Curso.objects.all()
    
    return render(request , "cursos.html" , {"cursos":curso})


def editar_curso(request , id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        
        mi_formulario = Curso_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            curso.nombre = datos["nombre"]
            curso.camada = datos["camada"]
            curso.save()
            
            curso = Curso.objects.all()
            return redirect(reverse('ver_cursos'))
        
    else:
        mi_formulario = Curso_formulario(initial={"nombre":curso.nombre , "camada":curso.camada})
    return render( request , "editar_curso.html" , {"mi_formulario": mi_formulario , "curso":curso})


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            contraseña = form.cleaned_data['contraseña']
            contraseña_hasheada = make_password(contraseña)
            form.save()
            return redirect('login')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('padre')              
            
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def padre(request):
    return render(request, 'padre.html')
        