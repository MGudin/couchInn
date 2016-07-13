from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ask/(?P<lodgment_id>[0-9]+)/$', views.ask, name='ask'),
    url(r'^answer/(?P<question_id>[0-9]+)/$', views.answer, name='answer'),
]

