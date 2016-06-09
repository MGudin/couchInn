from __future__ import unicode_literals

from django.db import models

#from app.lodgment.models import Place
# Create your models here.

class Gallery(models.Model):
    pass


class Photo(models.Model):
    title = models.CharField('titulo', max_length=20, default='untitled')
    photo = models.ImageField(upload_to='places')
    position = models.PositiveIntegerField(default=0)
    gallery = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE, editable=False)
