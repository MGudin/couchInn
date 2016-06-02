from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator 

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Solo caracteres alfanumericos son permitidos.')

class Category(models.Model):
    name = models.CharField('Nombre:', max_length=50, unique=True, validators=[alphanumeric])

    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.name



# Create your models here.
