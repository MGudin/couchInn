from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from . import forms

def signup(request):
    if request.method == 'POST':
        user_form = forms.CouchinnUserCreationForm(request.POST)
        if user_form.is_valid():
            print "paso el form"
            # user_form.save()
            request.user=user_form.save()
            return render(request, 'session/signup_succesfull.html')
        else:
            return render(request, 'session/signup.html',{'user_form': user_form})
    else:
        user_form = forms.CouchinnUserCreationForm()
    return render(request, 'session/signup.html', { 'user_form' : user_form })


@login_required
def profile(request):
    profile = request.user.couchinnuser
    return render(request, 'session/profile.html', {'profile':profile})
