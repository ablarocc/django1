from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from productos.models import Paleta
from django.urls import reverse_lazy
from django.views.generic.list import ListView


class CrearPaleta(CreateView):
    model = Paleta 
    template_name ='productos/crear_paleta.html'
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['color', 'escote', 'mangas']

class ListadoPaletas(ListView):
    model = Paleta
    template_name = "productos/listado_paletas.html"
    context_object_name = 'paletas'
    

# Create your views here.