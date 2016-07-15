import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator 

from crispy_forms.helper import FormHelper

from models import Place, Request
from app.backend.models import Category


# class LodgmentForm(forms.ModelForm):
#
#     def __init__(self, *args, **kwargs):
#         super(LodgmentForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.form_tag = False
#
#     initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
#     finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
#     category = forms.ModelChoiceField(queryset=Category.actives.all(), label='Tipo de hospedaje')
#
#     place  = forms.ModelChoiceField(queryset=Place.actives.all(), label='Couch')
#     class Meta:
#         model = Lodgment
#         exclude = ('create_date','reservations_taken','score','deleted','author')
#


class PlaceForm(forms.ModelForm):
#    photo = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(PlaceForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    category = forms.ModelChoiceField(queryset=Category.actives.all(), label='Tipo de hospedaje')

    class Meta:
        model = Place
        exclude = ('create_date','reservations_taken','score','deleted','user', 'gallery')
        widgets = {
            'name' : forms.TextInput,
            'direction' : forms.TextInput,
            'city' : forms.TextInput,
            'province' : forms.TextInput,
            }
    def clean(self):
        cleaned_data = super(PlaceForm, self).clean()
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


class PlaceEditForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PlaceEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Place
        widgets = {
            'name' : forms.TextInput,
            }
        exclude = ('create_date','reservations_taken','score','deleted','user',
                'gallery','city', 'direction', 'province', 'initial_date','finish_date','reservations_available')



class RequestForm(forms.ModelForm):

    initial_date = forms.ChoiceField(label='Fecha de inicio')
    finish_date = forms.ChoiceField(label='Fecha de fin')
    def __init__(self,*args, **kwargs):
        date_choices=kwargs.pop('date_choices')
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
       # self.fields['initial_date'].choices = date_choices
        initial_choices =(((date.strftime("%Y-%m-%d"), u"{}/{}/{}".format(date.day,date.month,date.year)) for date in date_choices))
        finish_choices =(((date.strftime("%Y-%m-%d"), u"{}/{}/{}".format(date.day,date.month,date.year)) for date in date_choices))
        self.fields['initial_date'].choices = initial_choices
        self.fields['finish_date'].choices = finish_choices


    class Meta:
        model = Request
        exclude = ('author', 'couch', 'create_date','state', 'score', 'host_score', 'tenant_score', 'host_scored', 'tenant_scored', 'date_accepted')

    def clean(self):
        cleaned_data = super(RequestForm, self).clean()
        try:
            today = datetime.datetime.now()
            init = cleaned_data.get('initial_date')
            end = cleaned_data.get('finish_date')
            init = datetime.datetime.strptime(init,'%Y-%m-%d')
            end  = datetime.datetime.strptime(end,'%Y-%m-%d')
            if today >= init or today >= end:
                raise forms.ValidationError('Las fechas tiene que ser mayores que la actual')
            if end <= init :
                raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
        except TypeError as e:
            print e

        return cleaned_data

class SearchForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}),required=False)
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}),required=False)
    category = forms.ModelChoiceField(queryset=Category.actives.all(), label='Tipo de hospedaje',required=False)
    city = forms.CharField(label='Ciudad',max_length=100,required=False)
    province = forms.CharField(label='Provincia',max_length=100,required=False)
    score = forms.FloatField(label='Valoracion', 
        validators = [
            MaxValueValidator(5),
            MinValueValidator(0)
            ]
        ,required=False
        )
    
    # def clean(self):
    #     print 'saraarararararasraarra'
    #     cleaned_data = super(SearchForm, self).clean()
    #     print cleaned_data
    #     try:
    #         today = datetime.date.today()
    #         init = cleaned_data.get('initial_date')
    #         end = cleaned_data.get('finish_date')
    #         if today >= init or today >= end:
    #             raise forms.ValidationError('Las fechas tiene que ser mayores que la actual')
    #         if end <= init :
    #             raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
    #     except TypeError as e:
    #         print e
    #
    #     return cleaned_data
   
class ScoreForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(ScoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    CHOICES = (( 1, 'mala',),
               ( 2, 'regular',),
               ( 3, 'buena',),
               ( 4, 'muy buena',),
               (5, 'excelente'))
    score = forms.ChoiceField(label='Seleccione un puntaje', widget=forms.RadioSelect, choices=CHOICES)
    review = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder' : 'Si lo desea puede dejar un comentario'}), required=False)
    
    
