from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^categoria/(?P<category_id>[0-9]+)/detalle/$', views.show_category, name='show_category'),
    url(r'^categoria/(?P<category_id>[0-9]+)/borrar/$', views.delete_category, name='delete_category'),
    url(r'^categoria/(?P<category_id>[0-9]+)/editar/$', views.edit_category, name='edit_category'),
    url(r'^categoria/nuevo/$', views.new_category, name='new_category'),
    url(r'^home/$', views.home, name='home'),
]
