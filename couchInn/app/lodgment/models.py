# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.auth.models import User

from app.backend.models import Category
from app.gallery.models import Gallery

# Create your models here.
class PlaceManager(models.Manager):
    def get_queryset(self):
        return super(PlaceManager, self).get_queryset().filter(deleted=False)

class Place(models.Model):
    name = models.TextField('Nombre', max_length=50)
    direction = models.TextField('Dirección', max_length=100)
    city = models.TextField('Ciudad', max_length=100)
    province = models.TextField('Provincia', max_length=100)
    score = models.FloatField('Valoración', default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        )
    user = models.ForeignKey(User, default=None, editable=False)
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, editable=False)
    deleted = models.BooleanField(default=False, editable=False)
    #managers
    objects = models.Manager()
    actives = PlaceManager()
    
    class Meta:
        verbose_name ='Inmueble'
        verbose_name_plural ='Inmuebles'

    def __str__(self):
        return self.name

    def is_used(self):
        # get all the lodgment related to me.
        # Then give me the ones wich are not currently in progress.
        # Finally... Is any in the queryset ??
        return self.lodgment_set.all().filter(finish_date__gt=date.today()).exists()

class LodgmentManager(models.Manager):
    def get_queryset(self):
        return super(LodgmentManager, self).get_queryset().filter(deleted=False)

class Lodgment(models.Model):
    title = models.CharField('Titulo', max_length=50, default='sin titulo')
    description = models.TextField('Descripción', max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    reservations_available = models.PositiveSmallIntegerField('Cantidad de personas',
            validators =[MinValueValidator(1)]
            )
    score = models.FloatField('Valoración', default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        )
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User, default=None)
    place = models.ForeignKey(Place, verbose_name=Place._meta.verbose_name)
    deleted = models.BooleanField(default=False)
    

    objects = models.Manager()
    actives = LodgmentManager()
    class Meta:
        verbose_name ='Hospedaje'
        verbose_name_plural ='Hospedajes'

    def is_used(self):
        return self.request_set.filter(state='acepted').exists()


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
    score = models.FloatField('Valoración', default=0, 
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
