from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField
# Create your models here.

class CouchinnUser(models.Model):
    AVAILABLE_GENDERS = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15, blank=False, null=False)
    nationality = CountryField()
    gender = models.CharField(max_length=1, choices=AVAILABLE_GENDERS)
    as_tenant_rank = models.SmallIntegerField(default=0)
    as_host_rank = models.SmallIntegerField(default=0)
    premium = models.BooleanField(default=False, editable=False)
    total_donations = models.PositiveIntegerField(default=0, editable=False)
