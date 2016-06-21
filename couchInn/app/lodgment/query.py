from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Lodgment, Place, Request
from django.db.models import Q

def simple_query(request):
    param = request.GET['params']
    if param:
        lodgments=Lodgment.actives.filter(Q(place__city=param) | Q(title=param) | Q(author__username=param)| Q(category__name=param))
    else:
        lodgments=Lodgment.actives.all()
    return render(request,'lodgment/index.html',{'lodgments':lodgments, 'params':param})
