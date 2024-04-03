from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path("", views.inicio , name="inicio"),
    
    path("ver_cursos", views.ver_cursos , name="ver_cursos"),
    path("alta_curso", views.curso_formulario),
    path("buscar_curso", views.buscar_curso),
    path("buscar", views.buscar , name="buscar"),
    path("elimina_curso/<int:id>" , views.elimina_curso , name="elimina_curso"),
    path("editar_curso/<int:id>" ,views.editar_curso , name="editar_curso"),
    
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('padre/', views.padre, name='padre'),
    
    path('alta_alumnos/', views.alumno_formulario, name='alta_alumnos'),
    path('ver_alumnos', views.ver_alumnos, name='ver_alumnos'), 
    
    
    path('alta_profesores/', views.profesor_formulario, name='alta_profesores'),
    path("ver_profesores/", views.ver_profesores , name="ver_profesores" ),
]

























