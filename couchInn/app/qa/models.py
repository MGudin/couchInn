from __future__ import unicode_literals

from django.db import models

# Create your models here.
from app.lodgment.models import Place
from app.session.models import CouchinnUser

class Question(models.Model):
    body = models.CharField('Pregunta', max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(CouchinnUser)
    couch = models.ForeignKey(Place)


# class Answer(models.Model):
#     body = models.CharField('Respuesta', max_length=250)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     user = models.ForeignKey(CouchinnUser)
#     question = models.OneToOneField(Question, on_delete=models.CASCADE)
    
