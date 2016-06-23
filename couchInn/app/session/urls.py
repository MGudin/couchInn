from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.core.urlresolvers import reverse
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
    url(r'^profile/editar$', views.edit_profile, name='edit_profile'),
    
    url(r'^password/reset/$',
        auth_views.password_reset,
        {'template_name':'session/forgot_password.html',#,
         'email_template_name': 'session/password_reset_email.html',
         'post_reset_redirect' : '/accounts/password/reset/done/',
#         'password_reset_form':forms.PasswordResetForm},
        },name='password_reset'),

    url(r'^password/reset/done/$',
        auth_views.password_reset_done ,
        {'template_name':'session/password_reset_done.html'},
        name='password_reset_done'),

    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name':'session/password_reset_confirm.html',
         'post_reset_redirect': '/accounts/reset/done/'},
        name='password_reset_confirm'),

    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {'template_name':'session/password_reset_complete.html'},
        name='password_reset_complete'),

]
