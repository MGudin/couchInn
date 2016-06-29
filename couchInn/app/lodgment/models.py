# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

from app.backend.models import Category
from app.gallery.models import Gallery

ESTADO={
        'pending':'pendiente',
        'reject':'rechazada',
        'acepted':'aceptada',
        }

# Create your models here.
class CouchManager(models.Manager):
    def get_queryset(self):
        return super(CouchManager, self).get_queryset().filter(deleted=False)

class Couch(models.Model):
    name = models.TextField('Nombre', max_length=50)
    description = models.TextField('Descripción', max_length=500)
    address = models.TextField('Direccion', max_length=100)
    city = models.TextField('Ciudad', max_length=100)
    province = models.TextField('Provincia', max_length=100)
    category = models.ForeignKey(Category)
    score = models.FloatField('Valoracion',
                              default=0, 
                              validators = [
                                  MaxValueValidator(5),
                                  MinValueValidator(0)
                              ])
    deleted = models.BooleanField(default=False, editable=False)
    guests = models.IntegerField('Huespedes', default=0)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    reservations_available = models.IntegerField('Cantidad de huespedes',
            validators =[MinValueValidator(1)]
            )

    
    user = models.ForeignKey(User, default=None, editable=False)
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, editable=False)
    
    #managers
    objects = models.Manager()
    actives = CouchManager()
    
    class Meta:
        verbose_name ='couch'
        verbose_name_plural ='couches'

    def __str__(self):
        return self.name

    def is_used(self):
        # get all the lodgment related to me.
        # Then give me the ones wich are not currently in progress.
        # Finally... Is any in the queryset ??
        return self.request_set.all().filter(finish_date__gt=date.today()).exists()

    def has_donation(self):
        return self.user.donation_set.exists()


class Request(models.Model):
    PENDING = 'PE'
    REJECTED = 'RJ'
    ACEPTED = 'AC'
    STATE_CHOICES = (
        (PENDING, 'pending'),
        (REJECTED, 'rejected'),
        (ACEPTED, 'acepted'),
    )
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=PENDING)
    author = models.ForeignKey(User)
    couch = models.ForeignKey(Couch)
    
    def __str__(self):
      return self.state


    class Meta:
        verbose_name ='Solicitud'
        verbose_name_plural ='Solicitudes'

    def get_state(self):
        return ESTADO[self.state] 



class Review(models.Model):
    text = models.TextField('Resenia', max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    score = models.FloatField('Valoración', default=0, 
        validators = [
          MaxValueValidator(5),
          MinValueValidator(0)
          ]
        )
    couch = models.ForeignKey(Couch)

    def __str__(self):
      return self.text

    class Meta:
        verbose_name ='Resenia'
        verbose_name_plural ='Resenias'

