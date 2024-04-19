from django.db import models
from django.contrib.auth.models import User  
from PIL import Image


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
    imagen_de_perfil = models.ImageField(upload_to="avatares" , null=True , blank=True)   
    
    def imagen_perfil_url(self):
        if self.imagen_de_perfil:
            return self.imagen_de_perfil.url
        else:
            return 'static/AppCoder/assets/img/robot-logo3.png'
    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.imagen_de_perfil:
            img = Image.open(self.imagen_de_perfil.path)
            output_size = (300, 300) 

            if img.height > 300 or img.width > 300:
                img.thumbnail(output_size)
                img.save(self.imagen_de_perfil.path)
    
    def __str__(self):
        return f"User: {self.user}  -  Imagen: {self.imagen_perfil_url()}"
    
    def crear_avatar_predeterminado(sender, instance, created, **kwargs):
        if created:
            avatar_predeterminado = Avatar(user=instance)
            avatar_predeterminado.save()
    




    

