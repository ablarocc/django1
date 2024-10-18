from django.urls import path
from inicio.views import inicio, segundo_template, crear_vestido,quienes_somos, buscar_modelo

urlpatterns = [
    path('', inicio, name='inicio'),
    path('Todos_los_vestidos/', segundo_template, name='Todos_los_vestidos'),
    path('vestidos', crear_vestido, name='vestidos'),
    path('quienes_somos', quienes_somos, name='nosotros'),
    path('buscar_modelo', buscar_modelo, name='buscar-modelo'),
    
]

    
