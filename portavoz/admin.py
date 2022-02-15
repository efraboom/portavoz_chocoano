from import_export import resources
from import_export.admin import ImportExportModelAdmin

from re import search
from django.contrib import admin
from portavoz.models import Palabra


class PalabraResource(resources.ModelResource):
    class Meta:
        model = Palabra

class PalabraAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    #Tabla
    list_display = (
        'nombre',
        'tipo',
        'clasificacion',
        'significado',
    )
    #buscador
    search_fields = ('nombre','significado',)
    #Filtro
    list_filter = ('tipo','clasificacion',)
    resource_class = PalabraResource

admin.site.register(Palabra,PalabraAdmin)
