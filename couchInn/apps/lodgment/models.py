from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nombre:', max_length=50)

    def __str__(self):
      return self.name
    

class Lodgment(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    reservations_taken = models.IntegerField(default=0)
    reservations_available = models.IntegerField('Cantidad de personas',
        validators =[MinValueValidator(1)]
        )
    score = models.FloatField('Valoracion', default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        )
    category = models.ForeignKey(Category)

    def vacancy(self):
      return self.reservations_available - self.reservations_taken

