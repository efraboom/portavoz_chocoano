from re import search
from django.contrib import admin
from portavoz.models import Palabra

# Register your models here.


class PalabraAdmin(admin.ModelAdmin):
    #Tabla
    list_display = (
        'nombre',
        'tipo',
        'clasificacion',
        'significado',
    )
    #buscador
    search_fields = ('nombre',)
    #Filtro
    list_filter = ('tipo','clasificacion',)

admin.site.register(Palabra,PalabraAdmin)