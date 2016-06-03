from django import forms
from django.core.exceptions import ValidationError
from models import Lodgment
from crispy_forms.helper import FormHelper
from app.backend.models import Category
import datetime

class LodgmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LodgmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    category = forms.ModelChoiceField(queryset=Category.actives.all(), label='Tipo de hospedaje')
    
    class Meta:
        model = Lodgment
        exclude = ('create_date','reservations_taken','score','deleted','author')

    def clean(self):
        cleaned_data = super(LodgmentForm, self).clean()
        try:
            init = cleaned_data.get('initial_date')
            end = cleaned_data.get('finish_date')
            if end < init :
                raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
        except TypeError as e:
            print e

        return cleaned_data
