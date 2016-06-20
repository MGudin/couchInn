import datetime
from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper

from models import Lodgment, Place, Request
from app.backend.models import Category


class LodgmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LodgmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    category = forms.ModelChoiceField(queryset=Category.actives.all(), label='Tipo de hospedaje')

    place  = forms.ModelChoiceField(queryset=Place.actives.all(), label='Couch')
    class Meta:
        model = Lodgment
        exclude = ('create_date','reservations_taken','score','deleted','author')

    def clean(self):
        cleaned_data = super(LodgmentForm, self).clean()
        try:
            today = datetime.date.today()
            init = cleaned_data.get('initial_date')
            end = cleaned_data.get('finish_date')
            if today >= init or today >= end:
                raise forms.ValidationError('Las fechas tiene que ser mayores que la actual')
            if end <= init :
                raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
        except TypeError as e:
            print e

        return cleaned_data


class PlaceForm(forms.ModelForm):
#    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Place
        exclude = ('score', 'user', 'gallery')
        widgets = {
            'name' : forms.TextInput,
            'direction' : forms.TextInput,
            'city' : forms.TextInput,
            'province' : forms.TextInput,
            }


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))

    class Meta:
        model = Request
        exclude = ('author', 'lodgment', 'create_date','state')

    def clean(self):
        cleaned_data = super(RequestForm, self).clean()
        try:
            today = datetime.date.today()
            init = cleaned_data.get('initial_date')
            end = cleaned_data.get('finish_date')
            if today >= init or today >= end:
                raise forms.ValidationError('Las fechas tiene que ser mayores que la actual')
            if end <= init :
                raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
        except TypeError as e:
            print e

        return cleaned_data
