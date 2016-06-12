from django import forms

from crispy_forms.helper import FormHelper

from .models import Photo

from .models import Photo

from .widgets import ImagePreviewWidget

class PhotoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False

    class Meta:
        model = Photo
        exclude = ('position','title')
        widgets = {
            'photo' : ImagePreviewWidget()
            }
            

class PhotoFormHelper(FormHelper):
    def __init__(self, *args, **kwargs):
        super(PhotoFormHelper, self).__init__(*args, **kwargs)
        self.form_tag = False
