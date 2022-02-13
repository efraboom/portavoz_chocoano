from tabnanny import verbose
from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Palabra(models.Model):
    nombre = CharField(max_length=200)
    tipo = CharField(max_length=50) 
    significado = TextField()
    clasificaciones = [
        ('afro', 'Afro'), 
        ('embera', 'Embera')
    ]
    clasificacion = CharField(max_length=16, choices=clasificaciones, default='afro') 

    class Meta:
        verbose_name = 'Listado de palabras'
        verbose_name_plural = 'Palabras'
        ordering = ['nombre']
        unique_together = ('nombre','significado','clasificacion')

    def __str__(self) -> str:
        return str(self.id) + '-' + self.nombre + '-' + self.clasificacion
