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

    #Paginador

    paginator = Paginator(palabras, 2)
    page = request.GET.get("page", 1)

    try:
        palabras = paginator.page(page)
    except PageNotAnInteger:
        palabras = paginator.page(1)
    except EmptyPage:
        palabras = paginator.page(paginator.num_pages)





    return render(request, 'resultados.html',{'palabras': palabras})

    

    #return render(request, 'resultados.html', {'palabras': palabras})
'''class Resultados(ListView):
    template_name = 'resultados.html'
    model = Palabra
    context_objetc_name = 'palabras'

    def buscar_palabra(self):
        busqueda = self.request.GET.get("busqueda","") #Obtiene las palabras escritas en el buscador
        palabra = Palabra.objects.filter(
        Q(nombre__icontains = busqueda) |
        Q(tipo__icontains  = busqueda) |
        Q(significado__icontains  = busqueda)
        ).distinct()
        print('resultado: ', palabra )
        return palabra
'''    



#RESULTADOS AFRO E INDIGENA
def afro(request):
    palabras = Palabra.objects.filter(clasificacion='afro')

    #Paginador

    paginator = Paginator(palabras, 2)
    page = request.GET.get("page", 1)

    try:
        palabras = paginator.page(page)
    except PageNotAnInteger:
        palabras = paginator.page(1)
    except EmptyPage:
        palabras = paginator.page(paginator.num_pages)

        
    return render(request, 'afro.html', {'palabras': palabras})

def indigena(request):
    palabras = Palabra.objects.filter(clasificacion='embera')
    return render(request, 'indigena.html',{'palabras': palabras})
 