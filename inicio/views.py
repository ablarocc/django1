
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import vestido
from inicio.forms import CrearVestidoForm
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
    
def crear_vestido(request, color, escote, mangas):
    Vestido = vestido(color = color, escote = escote, mangas = mangas)
    Vestido.save()
    
    return render(request, 'vestido.html', {'vestido': vestido})

def crear_vestido(request):
    
    #print ('Request', request)
    #print ('GET', request.GET)
    #print ('POST', request.POST)
    
    formulario = CrearVestidoForm()
    
    if request.method == 'POST':
      formulario = CrearVestidoForm(request.POST)
      if formulario.is_valid():
          data=formulario.cleaned_data
          Vestido = vestido(color = data.get('color'), escote = data.get('escote'), mangas = data.get('mangas'))
          Vestido.save()
          return redirect('inicio: buscar_modelo')
        

  
    return  render (request,'vestido.html', {'form': 'formulario'})
    
def buscar_modelo(request):
    return render(request, 'buscar_modelo.html', {'vestido': ''})
    
   
    
        



