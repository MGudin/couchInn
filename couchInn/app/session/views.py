from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import datetime

# Create your views here.
from . import forms
from .models import CouchinnUser
from app.lodgment.models import Request

def signup(request):
    if request.method == 'POST':
        user_form = forms.CouchinnUserCreationForm(request.POST)
        if user_form.is_valid():
            couchinnuser = user_form.save()
#            request.user=couchinnuser.user
            user = authenticate(username=request.POST['username'], password=request.POST['password1'])

            login(request, user)
            return render(request, 'session/signup_succesfull.html')
        else:
            return render(request, 'session/signup.html',{'user_form': user_form})
    else:
        user_form = forms.CouchinnUserCreationForm()
    return render(request, 'session/signup.html', { 'user_form' : user_form })


@login_required
def profile(request):
    today = datetime.date.today()
    profile = request.user.couchinnuser
    estadias_vencidas = Request.objects.filter(author=request.user).filter(finish_date__lt=today).filter(state='AC')
    couchs_vencidos = Request.objects.filter(couch__user=request.user).filter(finish_date__lt=today).filter(state='AC')
    return render(request, 'session/profile.html', {'profile':profile,
                                                    'estadias_vencidas': estadias_vencidas,
                                                    'couchs_vencidos':couchs_vencidos})

import pdb
@login_required
def edit_profile(request):
    user_profile = CouchinnUser.objects.get(pk=request.user.couchinnuser.pk)
    profile_form = forms.ProfileForm(request.POST or None, instance=user_profile)
    user_form = forms.UserForm(request.POST or None, instance=request.user)
    if request.method == 'POST':
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect(reverse('session:profile'))
    return render(request,'session/edit.html',{'profile_form': profile_form,
                                               'user_form': user_form})
    
