from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio , name="inicio"),
    path("perfil", views.perfil_usuario , name="perfil"),
    path('cargar_imagen/', views.cargar_imagen, name='cargar_imagen'),

    path("ver_cursos", views.ver_cursos , name="ver_cursos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar , name="buscar"),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" ,views.editar_curso , name="editar_curso"),
    
    path('register', views.register, name='Register'),
    path('login', views.login_request, name='login'),
    path("logout" , LogoutView.as_view(template_name="logout.html"), name="logout"),
   
    
    path('alta_alumnos/', views.alumno_formulario, name='alta_alumnos'),
    path('ver_alumnos/', views.ver_alumnos, name='ver_alumnos'), 
    path("elimina_alumno/<int:id>" , views.elimina_alumno , name="elimina_alumno"),
    path("editar_alumno/<int:id>" ,views.editar_alumno , name="editar_alumno"),
    
    
    path('alta_profesores/', views.profesor_formulario, name='alta_profesores'),
    path("ver_profesores/", views.ver_profesores , name="ver_profesores" ),
    path("elimina_profesor/<int:id>" , views.elimina_profesor , name="elimina_profesor"),
    path("editar_profesor/<int:id>" ,views.editar_profesor , name="editar_profesor"),
    
    path("nosostros", views.nosotros, name="Nosotros"),
    path("editarPerfil" , views.editarPerfil , name="EditarPerfil")
]

























