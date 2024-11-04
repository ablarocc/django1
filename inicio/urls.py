from django.urls import path
from inicio.views import (
    inicio,
    segundo_template,
    crear_vestido,
    quienes_somos,
    buscar_modelo,
    ver_modelo,
    eliminar_modelo,
    editar_modelo)
app_name = 'inicio'
urlpatterns = [
    path('', inicio, name='inicio'),
    path('Todos_los_vestidos', segundo_template, name='Todos-los-vestidos'),
    path('vestidos', crear_vestido, name='vestido'),
    path('quienes_somos', quienes_somos, name='quienes-somos'),
    path('buscar_modelo', buscar_modelo, name='buscar_modelo'),
    path('crear_vestido/<str:color>/<str:escote>/<str:mangas>/', crear_vestido, name = 'crear_vestido'),
    path('ver_vestido/<int:id>/', ver_modelo, name = 'ver_modelo'),
    path('eliminar_modelo/<int:id>/', eliminar_modelo, name = 'eliminar-modelo'),
    path('editar_modelo/<int:id>/', editar_modelo, name = 'editar-modelo')
]

    
