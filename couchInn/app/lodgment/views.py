# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Lodgment
from forms import LodgmentForm

def index(request):
    try:
        lodgments = Lodgment.objects.all()
    except e:
        print e
       
    return render(request,'lodgment/index.html',{'lodgments':lodgments})
# Create your views here.

def new(request):
    form_lodgment = LodgmentForm(request.POST or None)
    if form_lodgment.is_valid():
       lodgment = form_lodgment.save(commit=False)
       lodgment.save()
       return redirect(reverse('lodgment:detail', args=[lodgment.id]))
    return render(request,'lodgment/new.html',{'form':form_lodgment})

def detail(request,lodgment_id):
    lodgment = get_object_or_404(Lodgment, pk=lodgment_id)
    return render(request,'lodgment/detail.html',{'lodgment':lodgment})

def edit_lodgment(request, lodgment_id):
    lodgment = get_object_or_404(Lodgment, pk=lodgment_id)
    form = LodgmentForm(request.POST or None, instance = lodgment)
    if form.is_valid():
        form.save()
        return redirect(reverse('lodgment:index'))
    return render(request,'lodgment/edit_lodgment.html',{'form':form, 'lodgment':lodgment})

def delete_lodgment(request, lodgment_id):
    u = get_object_or_404(Lodgment, pk=lodgment_id)
    if u.is_used():
        u.deleted=True
        u.save()
    else:
        u.delete()

    return HttpResponseRedirect(reverse('lodgment:index'))
