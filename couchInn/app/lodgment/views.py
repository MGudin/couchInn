# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Lodgment
from forms import LodgmentForm
from django.contrib.auth.decorators import login_required

def index(request):
    try:
        lodgments = Lodgment.actives.all()
    except Exception as e:
        print e
       
    return render(request,'lodgment/index.html',{'lodgments':lodgments})
# Create your views here.

@login_required
def detail(request,lodgment_id):
    lodgment = get_object_or_404(Lodgment, pk=lodgment_id)
    return render(request,'lodgment/detail.html',{'lodgment':lodgment})

@login_required
def edit_lodgment(request, lodgment_id):
    lodgment = get_object_or_404(Lodgment, pk=lodgment_id)
    form = LodgmentForm(request.POST or None, instance = lodgment)
    if form.is_valid():
        form.save()
        return redirect(reverse('lodgment:index'))
    return render(request,'lodgment/edit_lodgment.html',{'form':form, 'lodgment':lodgment})

@login_required
def new(request):
    form_lodgment = LodgmentForm(request.POST or None)
    if form_lodgment.is_valid():
       lodgment = form_lodgment.save(commit=False)
       lodgment.author = request.user
       lodgment.save()
       return redirect(reverse('lodgment:detail', args=[lodgment.id]))
    return render(request,'lodgment/new.html',{'form':form_lodgment})

@login_required
def delete_lodgment(request, lodgment_id):
    u = get_object_or_404(Lodgment, pk=lodgment_id)
    if u.is_used():
        u.deleted=True
        u.save()
    else:
        u.delete()

    return HttpResponseRedirect(reverse('lodgment:index'))
