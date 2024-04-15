from django.shortcuts import render, redirect 
from AppCoder.models import Curso, Usuario, Alumnos, Profesores, Avatar
from django.http import HttpResponse
from django.template import loader
from AppCoder.forms import *
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required



#Alumnos

def ver_alumnos(request):
    alumnos = Alumnos.objects.all()
    return render(request, "ver_alumnos.html", {"alumnos": alumnos})

def alumno_formulario(request):
    if request.method == "POST":
        el_formulario = Alumnos_formulario(request.POST)
        if el_formulario.is_valid():
            datos = el_formulario.cleaned_data
            alumno = Alumnos(nombre=datos["nombre"], edad=datos["edad"], email=datos["email"])
            alumno.save()
            return redirect('ver_alumnos')  
    return render(request, "alta_alumnos.html")

def elimina_alumno(request, id):
    alumno = Alumnos.objects.get(id=id)
    alumno.delete()
    return redirect(reverse('ver_alumnos'))
        

def editar_alumno(request , id):
    alumno = Alumnos.objects.get(id=id)
    if request.method == "POST":
        
        el_formulario = Alumnos_formulario( request.POST )
        if el_formulario.is_valid():
            datos = el_formulario.cleaned_data
            alumno.nombre = datos["nombre"]
            alumno.edad = datos["edad"]
            alumno.email = datos["email"]
            alumno.save()
            
            alumno = Alumnos.objects.all()
            return redirect(reverse('ver_alumnos'))
        
    else:
        el_formulario = Alumnos_formulario(initial={"nombre":alumno.nombre , "edad":alumno.edad , "email":alumno.email})
    return render( request , "editar_alumno.html" , {"el_formulario": el_formulario , "alumno":alumno})




#Profesores
@login_required
def ver_profesores(request):
    profesores = Profesores.objects.all()
    return render(request, "ver_profesores.html", {"profesores": profesores})

def profesor_formulario(request):
    if request.method == "POST":
        su_formulario = Profesores_formulario(request.POST)
        if su_formulario.is_valid():
            datos = su_formulario.cleaned_data
            profesor = Profesores(nombre=datos["nombre"], asignatura=datos["asignatura"], email=datos["email"])
            profesor.save()
            return redirect('ver_profesores')  
    return render(request, "alta_profesores.html")

def elimina_profesor(request, id):
    profesor = Profesores.objects.get(id=id)
    profesor.delete()
    return redirect(reverse('ver_profesores'))
        

def editar_profesor(request , id):
    profesor = Profesores.objects.get(id=id)
    if request.method == "POST":
        
        su_formulario = Profesores_formulario( request.POST )
        if su_formulario.is_valid():
            datos = su_formulario.cleaned_data
            profesor.nombre = datos["nombre"]
            profesor.asignatura = datos["asignatura"]
            profesor.email = datos["email"]
            profesor.save()
            
            profesor = Profesores.objects.all()
            return redirect(reverse('ver_profesores'))
        
    else:
        su_formulario = Profesores_formulario(initial={"nombre":profesor.nombre , "asignatura":profesor.asignatura , "email":profesor.email})
    return render( request , "editar_profesor.html" , {"su_formulario": su_formulario , "profesor":profesor})


#Inicio
def inicio(request):
    avatar = None
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
    return render(request, "padre.html", {"avatar": avatar})

#Cursos

def alta_curso(request,nombre):
    curso = Curso(nombre=nombre , camada=234512)
    curso.save()
    texto = f"Se guardo en la BD el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)


def ver_cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos.html", {"cursos": cursos})


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
    
@login_required    
def elimina_curso(request , id):
    curso = Curso.objects.get(id=id).delete()     

    curso = Curso.objects.all()
    
    return render(request , "cursos.html" , {"cursos":curso})

@login_required
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


def register(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("Usuario creado")

    else:
        form = UserCreationForm()
    return render(request , "registro.html" , {"form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario , password=contra)
            if user is not None:
                login(request , user )  
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "inicio.html" , {"url":avatares[0].imagen.url})
            else:
                return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()
    return render( request , "login.html" , {"form":form})


def logout_request(request):
    return LogoutView.as_view(template_name='logout.html')(request)


def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        mi_formulario = UserEditForm(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request , "inicio.html")
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email})
    
    return render( request , "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})



def nosotros(request):
    return render(request, "nosotros.html" )

