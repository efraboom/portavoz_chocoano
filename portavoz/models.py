from django.db import models
from django.db.models.fields import CharField, TextField

# Create your models here.
class Palabra(models.Model):
    nombre = CharField(max_length=200)
    tipo = CharField(max_length=50) 
    significado = TextField()
    clasificaciones = [
        ('choco', 'Chocoano'), 
        ('embera', 'Indigena')
    ]
    clasificacion = CharField(max_length=16, choices=clasificaciones, default='choco') 
