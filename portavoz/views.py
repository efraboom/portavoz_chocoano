import random
from django.shortcuts import render
from django.db.models import Q
from portavoz.models import Palabra
from django.core.paginator import Paginator
from django.views.generic import TemplateView


#Inicio
def inicio(request):
    palabras = Palabra.objects.all()
    muestra = Palabra.objects.filter(id__range=[800,805])
    return render(request, 'inicio.html',{'muestra':muestra})

#Acerca de 
def acerca_de(request):
    return render(request, 'acerca_de.html')


#Resultados
def resultados(request):
    busqueda = request.GET.get('busqueda') #Obtiene las palabras escritas en el buscador

    if busqueda:
        palabras = Palabra.objects.filter(
            Q(nombre__icontains = busqueda) |
            Q(tipo__icontains  = busqueda) |
            Q(significado__icontains  = busqueda)
        ).distinct()#Filtra las busquedas

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
 
#Eror 404
'''def mi_error_404(request,exception):
    return render(request, 'not_founds.html', status=404) '''

#Errores 404 - 505
class ErrorView(TemplateView):
    template_name = "not_founds.html"
class Error505View(TemplateView):
    template_name = "not_founds.html"
    
    @classmethod
    def as_error_view(cls):
        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view


    

