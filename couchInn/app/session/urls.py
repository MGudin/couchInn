from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^logout/$', auth_views.logout,
            {
             'next_page':'/',
            },name='logout'),
    url(r'^login/$', auth_views.login,
            {
             'template_name':'session/login.html',
            },name='login'),
    url(r'^singnup/$', views.signup, name='signup'),
    url(r'^profile$', views.profile, name='profile'),
]
