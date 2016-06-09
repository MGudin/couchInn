from django.forms.widgets import FileInput
from django.utils.safestring import mark_safe
from django.conf import settings


class ImagePreviewWidget(FileInput):
    """ 
    Renders a FileInput with a thumbnail by it's side.Appends data
    attributes to said FileInput to update the thumbnail via
    javascript. Attributes added are: - data-thumbnail-trigger: use it
    to attach to 'change' event.  - data-target: id of img element to
    update.  
    """

    def render(self, name, value, attrs=None):
        output = (
            '<div class="row">'
            '<div class="col-md-4">{image_tag}</div>'
            '<div class="col-md-8">{file_input}</div>'
            '</div>'
        )

        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        image_id = "{id}thumbnail".format(id=final_attrs.get('id'))
        attrs.update({'data-target': image_id, 'data-thumbnail-trigger': True})

        image_tag = u'<img src="{url}" class="thumbnail" id="{id}">'
        # TODO: use thumbnail version of image if available
        if value and getattr(value, "url", None):
            image_url = value.url
        else:
            image_url = settings.MEDIA_URL + 'default-placeholder.png'

        image_tag = image_tag.format(url=image_url,id=image_id)
        file_input = super(ImagePreviewWidget, self).render(name, value, attrs)
        output = output.format(image_tag=image_tag, file_input=file_input)

        return mark_safe(output)
