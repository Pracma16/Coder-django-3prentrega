from django import forms
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Curso_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    camada = forms.IntegerField()
    
class Alumnos_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    edad = forms.IntegerField()  
    email = forms.EmailField(max_length=130)  
    
class Profesores_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    asignatura = forms.CharField(max_length=100)  
    email = forms.EmailField(max_length=130)      
    
class RegistroForm(forms.ModelForm):
    contraseña_confirmar = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'contraseña']
        widgets = {'contraseña': forms.PasswordInput}

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        contraseña_confirmar = cleaned_data.get('contraseña_confirmar')
        if contraseña != contraseña_confirmar:
            raise forms.ValidationError('Las contraseñas no coinciden.')


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}    