from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import LazyTypedChoiceField
from django_countries import countries
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from models import CouchinnUser



alphanumeric_validator = RegexValidator('^[A-Za-z0-9]+$',
                                         message='El valor deberia contener numeros y digitos')

numeric_validator = RegexValidator('^[0-9]+$',
                                   message='El valor debe contener solo numeros')

alphabetic_validator = RegexValidator('^[A-Za-z]+$',
                                      message='El valor debe contener solo letras del alfabeto')


class CouchinnUserCreationForm(UserCreationForm):
    GENDER_CHOICES = [('M', 'Masculino'), ('F','Femenino')]
    username = forms.CharField(label="usuario",
                               required=True,
                               validators=[alphanumeric_validator])
    first_name = forms.CharField(label='nombre',
                                 required=True,
                                 validators=[alphabetic_validator])
    last_name = forms.CharField(label='Apellido',
                                validators=[alphabetic_validator],
                                required=True)
    email = forms.EmailField(required=True)
    telephone = forms.CharField(label='telefono',
                                required=True,
                                validators=[numeric_validator])
    nationality = LazyTypedChoiceField(choices=countries)
    gender = forms.ChoiceField(label='Sexo',
                               choices=GENDER_CHOICES,
                               widget=forms.RadioSelect(),
                               required=True)


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email):
            raise ValidationError('El email ya esta en uso')
        return email
    
    def save(self, commit=True):
        user = super(CouchinnUserCreationForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        print user
        if commit:
            user.save()
            couchinn_user = CouchinnUser(user=user,
                                         telephone=self.cleaned_data["telephone"],
                                         nationality=self.cleaned_data["nationality"],
                                         gender=self.cleaned_data["gender"],
            )
            couchinn_user.save()
        return user
