from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User
from app.backend.models import Category

# Create your models here.
class Lodgment(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    score = models.FloatField('Valoracion', default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        )
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User, default=None)

    class Meta:
        verbose_name ='Hospedaje'
        verbose_name_plural ='Hospedajes'


class Request(models.Model):
    PENDING = 'PE'
    REJECTED = 'RJ'
    ACEPTED = 'AC'
    STATE_CHOICES = (
        (PENDING, 'en espera'),
        (REJECTED, 'rechazado'),
        (ACEPTED, 'aceptado'),
    )
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=PENDING)
    author = models.ForeignKey(User)
    lodgment = models.ForeignKey(Lodgment)
    
    def __str__(self):
      return self.state


    class Meta:
        verbose_name ='Solicitud'
        verbose_name_plural ='Solicitudes'


class Review(models.Model):
    text = models.TextField('Resenia', max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    score = models.FloatField('Valoracion', default=0, 
        validators = [
          MaxValueValidator(5),
          MinValueValidator(0)
          ]
        )
    lodgment = models.ForeignKey(Lodgment)

    def __str__(self):
      return self.text

    class Meta:
        verbose_name ='Resenia'
        verbose_name_plural ='Resenias'
