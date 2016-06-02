# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
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
       return redirect(reverse('lodgment:detail'))
    return render(request,'lodgment/new.html',{'form':form_lodgment})

def detail(request):
    return render(request,'lodgment/index.html')
