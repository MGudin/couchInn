# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator 

alphanumeric = RegexValidator(r'^[0-9a-zA-Z\s]*$', 'Solo caracteres alfanumericos son permitidos.')

class CategoryManager(models.Manager):
    def get_queryset(self):
        return super(CategoryManager, self).get_queryset().filter(deleted=False)

class Category(models.Model):
    name = models.CharField('Nombre:', max_length=50, unique=True, validators=[alphanumeric])
    deleted = models.BooleanField(default=False)

    objects = models.Manager()
    actives = CategoryManager()

    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural ='Categorias'

    def __str__(self):
        return self.name

    def is_used(self):
        return self.lodgment_set.exists()



# Create your models here.
