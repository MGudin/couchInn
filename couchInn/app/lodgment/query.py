from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Place, Request
from .forms import SearchForm
from django.db.models import Q
import datetime

def simple_query(request):
    get = request.GET
    param =get.get('params', False)
    if param:
        lodgments=Place.actives.filter(Q(city__icontains=param) | Q(title__icontains=param) | Q(user__username__icontains=param)| Q(category__name__icontains=param))
    else:
        lodgments=Place.actives.all()
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
    lodgments = Place.actives.all()
    if form.is_valid():
        if score:
            lodgments = lodgments.filter(score=score)
        if city:
            lodgments = lodgments.filter(city__icontains=city)
        if province:
            lodgments = lodgments.filter(province__icontains=province)
        if category:
            lodgments = lodgments.filter(category=category)
        if finish_date:
            finish_date = datetime.datetime.strptime(finish_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            lodgments = lodgments.filter(finish_date__gte=finish_date).order_by('initial_date')

        else:
            finish_date = datetime.date.today().strftime("%Y-%m-%d")
        if initial_date:
            initial_date = datetime.datetime.strptime(initial_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            if initial_date >= finish_date:
                finish_date = initial_date

            lodgments = lodgments.filter(Q(finish_date__gte=finish_date) & Q (initial_date__lte=initial_date))
        return render(request,'lodgment/detail_search.html',{'lodgments':lodgments,'form':form})
    return render(request,'lodgment/detail_search.html',{'lodgments':lodgments, 'form':form})
