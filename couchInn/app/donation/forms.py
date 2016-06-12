from django import forms
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from crispy_forms.bootstrap import AppendedText
from .models import Donation
from django.core.validators import int_list_validator, MaxLengthValidator, MinLengthValidator, MinValueValidator, RegexValidator

import pdb

only_numbers_validator = int_list_validator(sep='',
                                            message='El campo debe contener solo numeros')
max_length_validator_cc = MaxLengthValidator(24,
                                          message='El campo debe tener 24 numeros')
min_length_validator_cc = MinLengthValidator(24,
                                          message='El campo debe tener 24 numeros')

positive_integer_validator_dn = MinValueValidator(1, message='El numero de documento no es correcto')

only_alphabetical_chars_validator_fn = RegexValidator(r'^[a-zA-Z]*$', 'Solo caracteres alfabeticos son permitidos.')
class DonationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DonationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.label_class="col-md-4"
        self.helper.field_class="col-md-8"
        self.helper.form_tag = False
        

    card_number = forms.CharField(label="ingrese el numero de tarjeta",
                                  validators=[only_numbers_validator,
                                              max_length_validator_cc,
                                              min_length_validator_cc],
                                  widget=forms.TextInput,
                                  required=True)
    document_number = forms.IntegerField(label="Numero de documento del titular",
                                         widget=forms.TextInput,
                                         validators=[positive_integer_validator_dn])
    full_name = forms.CharField(label="Nombre completo del titular de la tarjeta",
                                validators=[only_alphabetical_chars_validator_fn])

    class Meta:
        model = Donation
        fields = ('amount',)
