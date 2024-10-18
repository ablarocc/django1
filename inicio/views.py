from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime
from django.shortcuts import render
from inicio.models import vestido

def inicio(request):
    return render(request, 'inicio.html')
    # return HttpResponse('<h1>Soy la pantalla de inicio </h1>')

#def vista_datos(request, nombre):
    #nombre_mayuscula = nombre.upper()
    #return HttpResponse(f'HOLA {nombre_mayuscula}')

def quienes_somos (request):
    return render(request, 'About.html')
    
def segundo_template(request):
    
    fecha_actual = datetime.now()
    datos = {
        'fecha_actual': fecha_actual,
        'numeros': list(range(1, 15))
    }
    #archivo_del_template = open(r'templates\segundo_template.html')
    #template = Template(archivo_del_template.read())
    #archivo_del_template.close()
    #contexto = Context(datos)
    #render_template =template.render(contexto)
    
    #opcion 2
    #template = loader.get_template('segundo_template.html')
    #render_template = template.render(datos)
    
    #opcion 3
    return render(request, 'segundo_template.html', datos)
    
    #return HttpResponse(render_template)
    
def guardar_vestido(request, color, escote, mangas):
    Vestido = vestido(color = color, escote = escote, mangas = mangas)
    Vestido.save()
    return render(request, 'vestido.html', {'vestido': Vestido})
   
    
        


# Create your views here.
