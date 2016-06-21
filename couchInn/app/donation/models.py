from __future__ import unicode_literals
from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.
min_amount_validator = MinValueValidator(2, message="el monto no puede ser inferior a $1")
class Donation(models.Model):

    amount = models.PositiveIntegerField('Donacion',
                                         default=2,
                                         validators=[min_amount_validator])
    donation_date = models.DateField(editable=False, auto_now_add=True)

    user = models.ForeignKey(User, default=None, editable=False)
