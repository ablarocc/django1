from django.urls import path
from productos import views

app_name = 'productos'
urlpatterns = [
    path('paletas/crear/', views.CrearPaleta.as_view(), name='crear_paleta'),
    path('paletas/', views.ListadoPaletas.as_view(), name='listado_paletas'),
]
