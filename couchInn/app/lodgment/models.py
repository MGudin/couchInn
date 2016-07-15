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
class PlaceManager(models.Manager):
    def get_queryset(self):
        return super(PlaceManager, self).get_queryset().filter(deleted=False)#.order_by('-user__donation__amount')



class Place(models.Model):
    title = models.CharField('Titulo', max_length=50, default='sin titulo')
    direction = models.TextField('Direccion', max_length=100)
    city = models.TextField('Ciudad', max_length=100)
    province = models.TextField('Provincia', max_length=100)
    user = models.ForeignKey(User, default=None, editable=False)
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, editable=False)
    deleted = models.BooleanField(default=False, editable=False)
    description = models.TextField('Descripción', max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    initial_date = models.DateField('Fecha de inicio')
    finish_date = models.DateField('Fecha de fin')
    reservations_available = models.PositiveSmallIntegerField('Cantidad de personas',
            validators =[MinValueValidator(1)]
            )
    score = models.PositiveSmallIntegerField('Valoración', default=0, 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        )
    category = models.ForeignKey(Category)
    deleted = models.BooleanField(default=False)
    #managers
    objects = models.Manager()
    actives = PlaceManager()
    
    class Meta:
        verbose_name ='Couch'
        verbose_name_plural ='Couchs'

    def __str__(self):
        return self.title

    def is_used(self):
        return self.request_set.filter(state='AC').exists()

    def has_donation(self):
        return self.user.donation_set.exists()

    def have_space(self):
        return (self.reservations_available > self.request_set.filter(state='AC').count())

    def auto_reject(self):
        self.request_set.filter(state='PE').update(state='RJ')
#
# class Lodgment(models.Model):
#     title = models.CharField('Titulo', max_length=50, default='sin titulo')
#     description = models.TextField('Descripción', max_length=500)
#     create_date = models.DateTimeField(auto_now_add=True)
#     initial_date = models.DateField('Fecha de inicio')
#     finish_date = models.DateField('Fecha de fin')
#     reservations_available = models.PositiveSmallIntegerField('Cantidad de personas',
#             validators =[MinValueValidator(1)]
#             )
#     score = models.FloatField('Valoración', default=0, 
#         validators = [
#             MaxValueValidator(5),
#             MinValueValidator(0)
#             ]
#         )
#     category = models.ForeignKey(Category)
#     author = models.ForeignKey(User, default=None)
#     place = models.ForeignKey(Place, verbose_name=Place._meta.verbose_name)
#     deleted = models.BooleanField(default=False)
#     
#
#     objects = models.Manager()
#     actives = LodgmentManager()
#     class Meta:
#         verbose_name ='Hospedaje'
#         verbose_name_plural ='Hospedajes'
#
#     def is_used(self):
#         return self.request_set.filter(state='acepted').exists()
#
#     def has_donation(self):
#         return self.author.donation_set.exists()


class Request(models.Model):
    PENDING = 'PE'
    REJECTED = 'RJ'
    ACEPTED = 'AC'
    STATE ={
            PENDING: u'Pendiente',
            REJECTED: u'Rechazada',
            ACEPTED: u'Aceptada',
            }
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
    couch = models.ForeignKey(Place)
    host_score = models.PositiveSmallIntegerField('Valoración', default=0, 
        validators = [
          MaxValueValidator(5),
          MinValueValidator(0)
          ]
        )
    tenant_score = models.PositiveSmallIntegerField('Valoración', default=0, 
                                                  validators = [
                                                      MaxValueValidator(5),
                                                      MinValueValidator(0)
                                                  ])
    host_scored = models.BooleanField(default=False)
    tenant_scored = models.BooleanField(default=False)

    date_accepted = models.DateField('fecha de aceptacion')

    
    def __str__(self):
      return self.state


    class Meta:
        verbose_name ='Solicitud'
        verbose_name_plural ='Solicitudes'

    def get_state(self):
        return self.STATE[self.state] 



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
    couch = models.ForeignKey(Place)

    def __str__(self):
      return self.text

    class Meta:
        verbose_name ='Resenia'
        verbose_name_plural ='Resenias'

