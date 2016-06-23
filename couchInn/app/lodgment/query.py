from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Lodgment, Place, Request
from .forms import SearchForm
from django.db.models import Q
import datetime

def simple_query(request):
    get = request.GET
    param =get.get('params', False)
    if param:
        lodgments=Lodgment.actives.filter(Q(place__city=param) | Q(title=param) | Q(author__username=param)| Q(category__name=param))
    else:
        lodgments=Lodgment.actives.all()
    return render(request,'lodgment/index.html',{'lodgments':lodgments, 'params':param})


def advance_query(request):
    get = request.GET
    category = get.get('category', False)
    city = get.get('city', False)
    score = get.get('score', False)
    province = get.get('province', False)
    initial_date = get.get('initial_date', False)
    finish_date = get.get('finish_date', False)
    form = SearchForm(request.GET or None)
    lodgments = Lodgment.actives.all()
    if form.is_valid():
        if score:
            lodgments = lodgments.filter(place__score=score)
        if city:
            lodgments = lodgments.filter(place__city=city)
        if province:
            lodgments = lodgments.filter(place__province=province)
        if category:
            lodgments = lodgments.filter(category=category)
        if finish_date:
            finish_date = datetime.datetime.strptime(finish_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            lodgments = lodgments.filter(finish_date__gte=finish_date).order_by('initial_date')

        else:
            finish_date = datetime.date.today()
        if initial_date:
            initial_date = datetime.datetime.strptime(initial_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            lodgments = lodgments.filter(Q(finish_date__gte=finish_date) & Q (initial_date__lte=initial_date))
        return render(request,'lodgment/detail_search.html',{'lodgments':lodgments,'form':form})
    return render(request,'lodgment/detail_search.html',{'lodgments':lodgments, 'form':form})
