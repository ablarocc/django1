from django.urls import path
from inicio.views import inicio, segundo_template, guardar_vestido,quienes_somos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('Todos_los_vestidos/', segundo_template, name='Todos_los_vestidos'),
    path('vestidos', guardar_vestido, name='vestidos'),
    path('quienes_somos', quienes_somos, name='nosotros'),
]

    
