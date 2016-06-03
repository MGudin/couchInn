from django import forms
from django.core.exceptions import ValidationError
from models import Category, Lodgment

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']


class LodgmentForm(forms.ModelForm):
    initial_date = forms.DateField(label='Fecha de inicio',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    finish_date = forms.DateField(label='Fecha de fin',input_formats=['%d/%m/%Y'], widget= forms.DateInput(attrs={'class':'datepicker'}))
    
    class Meta:
        model = Lodgment
        exclude = ('create_date','reservations_taken','score')

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