from django import forms
from django.core.validators import MaxLengthValidator

from crispy_forms.helper import FormHelper

from .models import Question



class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False

    def clean(self):
        cleaned_data = super(QuestionForm, self).clean()
        body = self.cleaned_data.get('body')
        max_length = MaxLengthValidator(250, message='El texto ingresado es muy largo')
        max_length(body)

        
    class Meta:
        model = Question
        fields = [ 'body', ]
        widgets = { 'body': forms.Textarea(attrs={'cols':50, 'rows':5, 'placeholder' : 'hace tu pregunta'})}
