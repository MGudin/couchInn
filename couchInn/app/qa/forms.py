from django import forms

from crispy_forms.helper import FormHelper

from .models import Question

class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.form_show_labels = False

    class Meta:
        model = Question
        fields = [ 'body', ]
        widgets = { 'body': forms.Textarea(attrs={'cols':50, 'rows':5, 'placeholder' : 'hace tu pregunta'})}
