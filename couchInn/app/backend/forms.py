from django import forms
from django.core.exceptions import ValidationError
from models import Category
from crispy_forms.helper import FormHelper


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
    
    class Meta:
        model = Category
        fields = ['name']

