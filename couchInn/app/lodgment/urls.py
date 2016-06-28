"""couchInn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
    Examples:
        Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
        Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
        Including another URLconf
        1. Import the include() function: from django.conf.urls import url, include
        2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
        """
from django.conf.urls import url
from . import views
from . import query

urlpatterns = [
    url(r'^hospedaje/(?P<lodgment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^hospedaje/editar/(?P<lodgment_id>[0-9]+)/$', views.edit_lodgment, name='edit_lodgment'),
    url(r'^hospedaje/borrar/(?P<lodgment_id>[0-9]+)/$', views.delete_lodgment, name='delete_lodgment'),
    url(r'^solicitud/(?P<lodgment_id>[0-9]+)/$', views.new_request, name='new_request'),
    url(r'^mis_hospedajes/$', views.user_lodgment, name='user_lodgment'),
    url(r'^mis_solicitudes/$', views.request_index, name='request_index'),
    url(r'^nuevo/$', views.new, name='new'),
    url(r'^couch/eliminar/(?P<place_id>[0-9]+)/$', views.delete_place, name='delete_place'),
    url(r'^couch/editar/(?P<place_id>[0-9]+)/$', views.edit_place, name='edit_place'),
    url(r'^couch/(?P<place_id>[0-9]+)/$', views.show_place, name='show_place'),
    url(r'^couch/nuevo$', views.create_place, name='new_place'),
    url(r'^mis_couchs/$', views.index_place, name='index_place'),
    url(r'^busqueda/$', query.simple_query, name='simple_query'),
    url(r'^busqueda_avanzada/$', query.advance_query, name='advance_query'),
    url(r'^$', views.index, name='index'),
]
