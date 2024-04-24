from django import forms
from .models import Usuario
from django.contrib.auth.models import User
from .models import Avatar


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
     

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label="Nombre de usuario", max_length=150)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        help_text = {k:"" for k in fields}

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen_de_perfil']        