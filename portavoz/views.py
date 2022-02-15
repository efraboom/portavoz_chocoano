from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Q
from portavoz.models import Palabra
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger

# Create your views here.

#Inicio
def inicio(request):
    return render(request, 'inicio.html')

#Acerca de 
def acerca_de(request):
    return render(request, 'acerca_de.html')

#Eror 404
def mi_error_404(request,exception):
    return render(request, 'not_founds.html', status=404) 

#Resultados
def resultados(request):
    busqueda = request.GET.get('busqueda') #Obtiene las palabras escritas en el buscador
    #palabras = Palabra.objects.filter(nombre=busqueda)
    #palabras = Palabra.objects.all()

    if busqueda:
        palabras = Palabra.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(tipo__icontains  = busqueda) |
            Q(significado__icontains  = busqueda)
        ).distinct()

    # Set up paginator
    p = Paginator(palabras, 10)
    page = request.GET.get('page')
    verbal = p.get_page(page)

    return render(request, 'resultados.html',{'palabras': palabras, 'verbal': verbal, 'busqueda':busqueda}) 

#RESULTADOS AFRO E INDIGENA
def afro(request):
    palabras = Palabra.objects.filter(clasificacion='afro')

    # Set up paginator
    p = Paginator(palabras, 10)
    page = request.GET.get('page')
    verbal = p.get_page(page)
    return render(request, 'afro.html', {'palabras': palabras, 'verbal': verbal})

def indigena(request):
    palabras = Palabra.objects.filter(clasificacion='Embera Dóbida')

    # Set up paginator
    p = Paginator(palabras, 10)
    page = request.GET.get('page')
    verbal = p.get_page(page)
    return render(request, 'indigena.html', {'palabras': palabras, 'verbal': verbal})
 