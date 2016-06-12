from django.conf.urls import url, include

from . import views
urlpatterns = [
    url(r'^donar/$', views.donate, name="donate" ),
    url(r'^donaciones/$', views.donation_index, name="index" ),

]
