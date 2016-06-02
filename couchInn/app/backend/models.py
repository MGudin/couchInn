from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Category(models.Model):
  name = models.CharField('Nombre:', max_length=50, unique=True)
  reservations_available = models.IntegerField('Cantidad de personas',
        validators =[MinValueValidator(1)]
        )

  def __str__(self):
      return self.name



# Create your models here.
