from django.db import models
from django.contrib.auth.models import User

class Alumnos(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    email = models.EmailField(max_length=154)  

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.email}"

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField() 
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100, unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario
        
class Profesores(models.Model):
    nombre = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    
    def __str__(self):
        return f"Nombre: {self.nombre}  Asignatura: {self.asignatura} Email: {self.email} "
    

class Avatar(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares" , null=True , blank=True)
    
    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen}"

