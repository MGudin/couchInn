# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory

from .models import Lodgment, Place
from .forms import LodgmentForm, PlaceForm
from app.gallery.forms import PhotoForm
from app.gallery.models import Gallery, Photo

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


def create_place(request):
    place_form = PlaceForm(request.POST or None)
    PForm = formset_factory(PhotoForm, extra=3)
    photo_form = PForm(request.POST or None, request.FILES or None)
    import pdb;
    if request.method == 'POST':
        if place_form.is_valid() and photo_form.is_valid():
            gallery = Gallery()
            gallery.save()
            place = place_form.save(commit=False)
            place.user = request.user
            place.gallery = gallery
            place.save()
            for form in photo_form:
                if form:
                    photo = form.save(commit=False)
                    photo.place = place
                    photo.gallery = gallery
                    photo.save()            
            return HttpResponseRedirect(reverse('lodgment:index_place'))

    return render(request,'place/new.html', {'place_form' : place_form,
                                             'photo_form': photo_form })

def index_place(request):
    places = Place.objects.all()
    return render(request, 'place/index.html',{'places': places})
