# -*- coding: utf-8 -*-
from django import forms
from django.core.exceptions import ValidationError
from models import Category
from crispy_forms.helper import FormHelper
import datetime

class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
    
    class Meta:
        model = Category
        fields = ['name']


class DateFilterForm(forms.Form):
    initial_date = forms.DateField(label='Fecha de inicio',
                                   input_formats=['%d/%m/%Y'],
                                   widget= forms.DateInput(attrs={'class':'datepicker',
                                                                  'placeholder':'fecha de inicio'}))
    finish_date = forms.DateField(label='Fecha de fin',
                                  input_formats=['%d/%m/%Y'],
                                  widget= forms.DateInput(attrs={'class':'datepicker',
                                                                 'placeholder':'fecha de fin'}))

    def __init__(self, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    
    def clean(self):
        cleaned_data = super(DateFilterForm, self).clean()
        # try:
        #     today = datetime.date.today()
        init = cleaned_data.get('initial_date')
        end = cleaned_data.get('finish_date')
        if end < init :
            raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
            
        return cleaned_data


class RequestFilterForm(forms.Form):


    initial_date_s = forms.DateField(label='Fecha de inicio',
                                   input_formats=['%d/%m/%Y'],
                                   widget= forms.DateInput(attrs={
                                                                  'placeholder':'fecha de inicio',
                                                                  'id':'datepicker2'}))
    finish_date_s = forms.DateField(label='Fecha de fin',
                                  input_formats=['%d/%m/%Y'],
                                  widget= forms.DateInput(attrs={
                                                                 'placeholder':'fecha de fin',
                                                                 'id': 'datepicker3'}))

    def __init__(self, *args, **kwargs):
        super(RequestFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

        
    def clean(self):
        cleaned_data = super(RequestFilterForm, self).clean()
        # try:
        #     today = datetime.date.today()
        init = cleaned_data.get('initial_date_s')
        end = cleaned_data.get('finish_date_s')
        if end < init :
            raise forms.ValidationError('La fecha de fin tiene que ser mayor que la de inicio')
            
        return cleaned_data

