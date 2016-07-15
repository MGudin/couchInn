# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.contrib import messages
from dateutil import rrule, parser

from .models import Place, Request
from .forms import PlaceForm, RequestForm, PlaceEditForm, ScoreForm
from app.gallery.forms import PhotoForm, PhotoFormHelper
from app.gallery.models import Gallery, Photo
from app.gallery.widgets import ImagePreviewWidget
from datetime import datetime
from app.qa.forms import QuestionForm
from app.qa.models import Question

# for development
import pdb;

def index(request):
    today = datetime.today()
    try:
        lodgments = Place.actives.all()#.exclude(finish_date__lt=today)
    except Exception as e:
        print e
    # si hay usuario logueado traete las solicitudes que no 
    # puntuo como inquilino
    if request.user.is_authenticated():
        estadias_sin_puntuar = Request.objects.filter(author=request.user).filter(finish_date__lt=today).filter(host_scored=False)
    else:
       estadias_sin_puntuar = None
    # si hay usuario logueado traete las solicitudes que no 
    # puntuo como dueño del couch
    if request.user.is_authenticated():
        inquilinos_sin_puntuar = Request.objects.filter(couch__user=request.user).filter(finish_date__lt=today).filter(tenant_scored=False)
    else:
       inquilinos_sin_puntuar = None
    return render(request,'lodgment/index.html',{'lodgments':lodgments,
                                                 'estadias_sin_puntuar': estadias_sin_puntuar,
                                                 'inquilinos_sin_puntuar': inquilinos_sin_puntuar})
# Create your views here.

@login_required
def detail(request,lodgment_id):
    lodgment = get_object_or_404(Place, pk=lodgment_id)
    if request.session.has_key('post_data'):
        post_data = request.session.pop('post_data')
    else:
        post_data = None
        
    question_form = QuestionForm(post_data)
    questions = lodgment.question_set.all().order_by('-created_at')
    return render(request,'lodgment/detail.html',{'lodgment':lodgment,
                                                  'question_form': question_form,
                                                  'questions': questions})

@login_required
def edit_lodgment(request, lodgment_id):
    lodgment = get_object_or_404(Place, pk=lodgment_id)
    form = PlaceEditForm(request.POST or None, instance = lodgment)
    if form.is_valid():
        form.save()
        return redirect(reverse('lodgment:index'))
    return render(request,'lodgment/edit_lodgment.html',{'form':form, 'lodgment':lodgment})

@login_required
def new(request):
    form_lodgment = PlaceForm(request.POST or None)
    if form_lodgment.is_valid():
       lodgment = form_lodgment.save(commit=False)
       lodgment.user = request.user
       lodgment.save()
       return redirect(reverse('lodgment:detail', args=[lodgment.id]))
    return render(request,'lodgment/new.html',{'form':form_lodgment})

@login_required
def delete_lodgment(request, lodgment_id):
    place = get_object_or_404(Place, pk=lodgment_id)
    if place.is_used():
        messages.warning(request, 'El couch ya tiene solicitudes aceptadas.')
    else:
        messages.success(request, 'El couch ha sido eliminado.')
        print request
        place.delete()
    return HttpResponseRedirect(reverse('lodgment:index_place'))

@login_required
def create_place(request):
    place_form = PlaceForm(request.POST or None)
    PForm = formset_factory(PhotoForm, extra=3)
    photo_form = PForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if place_form.is_valid() and photo_form.is_valid():
            gallery = Gallery()
            gallery.save()
            place = place_form.save(commit=False)
            place.user = request.user
            place.gallery = gallery
            place.save()
            for form in photo_form:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.place = place
                    photo.gallery = gallery
                    photo.save()            
            return HttpResponseRedirect(reverse('lodgment:index_place'))

    return render(request,'place/new.html', {'place_form' : place_form,
                                             'photo_form': photo_form })
@login_required
def index_place(request):
    places = Place.objects.filter(user=request.user)

    return render(request, 'place/index.html',{'places': places})

@login_required
def show_place(request,place_id):
    question_form = QuestionForm()
    question_form.body = request.session['answer_body']
    place = Place.objects.get(pk=place_id)
    return render(request, 'place/show_place.html',{'place': place,
                                                    'question_form' : question_form})


@login_required
def edit_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_form = PlaceEditForm(request.POST or None,instance=place)
    PForm = inlineformset_factory(Gallery,
                                  Photo,
                                  fields=('photo',),
                                  form = PhotoForm,
                                  widgets={'photo': ImagePreviewWidget},
                                  min_num=0,
                                  validate_min = True,
                                  can_delete=True,
                                  max_num=3)
    photo_form = PForm(request.POST or None,
                       request.FILES or None,
                       instance=place.gallery)
    photo_form.helper = PhotoFormHelper()
    if request.method == 'POST':
        if photo_form.is_valid() and place_form.is_valid():
            place_form.save()
            for form in photo_form:
                if form.cleaned_data:
#                    pdb.set_trace()
                    if form.cleaned_data['DELETE'] == True:
                        form.cleaned_data['id'].delete()
                    else:
                        
                        form.save()
            return redirect(reverse('lodgment:detail',args=place_id))

    return render(request, 'place/edit.html',{'place_form': place_form,
                                              'photo_form': photo_form,
                                              'place': place})
@login_required
def delete_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    if place.is_used():
        messages.error(request, 'El couch ya tiene solicitudes aceptadas.')
    else:
        messages.success(request, 'El couch ha sido eliminado.')
        print request.messages
        place.delete()
    return HttpResponseRedirect(reverse('lodgment:index_place'))

@login_required
def user_lodgment(request):
    try:
        lodgments = Place.actives.filter(user=request.user)
    except Exception as e:
        print e
       
    return render(request,'lodgment/index.html',{'lodgments':lodgments})


@login_required
def new_request(request, lodgment_id):
    try:
        lodgment = Place.actives.get(pk=lodgment_id)
    except Exception as e:
        messages.error(request, 'El couch solicitado no existe mas.')
        return redirect(reverse('lodgment:index'))
    date_choices=tuple(rrule.rrule(3,
        dtstart=lodgment.initial_date,
        until=lodgment.finish_date))
    form = RequestForm(request.POST or None,date_choices=date_choices)
    print form.is_valid()
    if form.is_valid():
       initial_date = form.cleaned_data.get('initial_date')
       finish_date = form.cleaned_data.get('finish_date')
       print initial_date, finish_date
       n_request = form.save(commit=False)
       n_request.author = request.user
       n_request.state = 'PE'
       n_request.couch = lodgment
       messages.success(request, 'La solicitud a sido enviada.')
       n_request.save()
       return redirect(reverse('lodgment:index'))
    return render(request,'lodgment/new_request.html',{'form':form, 'lodgment_id':lodgment_id})


@login_required
def request_index(request):
    try:
        requests = Request.objects.filter(author=request.user)
        print requests
    except Exception as e:
        print e
    return render(request,'lodgment/request_index.html',{'requests':requests})

@login_required
def detail_request(request,lodgment_id):
    try:
        place = Request.objects.get(pk=lodgment_id)
    except Exception as e:
        print e
    return render(request,'lodgment/request_detail.html',{'request':place})

@login_required
def couch_request(request):
    try:
        requests = Request.objects.filter(couch__user=request.user).filter(state='PE')
    except Exception as e:
        print e
    return render(request,'lodgment/couch_request.html',{'requests':requests})

@login_required
def acept_request(request,lodgment_id):
    try:
        place = Request.objects.get(pk=lodgment_id)
        if place.couch.have_space():
            place.state='AC'
            place.save()
            messages.success(request, 'La solicitud a sido aceptada.')
            if not place.couch.have_space():
                place.couch.auto_reject()
        else:
            messages.warning(request, 'El couch ya no tiene lugar.')

        requests = Request.objects.filter(couch__user=request.user).filter(state='PE')

    except Exception as e:
        print e

    return HttpResponseRedirect(reverse('lodgment:couch_request'))


@login_required
def reject_request(request,lodgment_id):
    try:
        place = Request.objects.get(pk=lodgment_id)
        place.state='RJ'
        place.save()
        messages.success(request, 'La solicitud a sido rechazada.')
        requests = Request.objects.filter(couch__user=request.user).filter(state='PE')
    except Exception as e:
        print e

    return HttpResponseRedirect(reverse('lodgment:couch_request'))

@login_required
def history(request):
    today = datetime.today()
    couchs = Request.objects.filter(author=request.user).filter(state='AC').filter(finish_date__lt=today)

    return render(request,'lodgment/history.html',{'lodgments':couchs})



@login_required
def score_couch(request, request_id):
    form = ScoreForm(request.POST or None)
    req = get_object_or_404(Request, pk=request_id)
    couch = req.couch
    if request.method == 'POST':
        if form.is_valid():
            score = form.cleaned_data['score']
            score = int(score)
            couch.score = score
            req.host_scored = True
            couch.user.couchinnuser.as_tenant_rank = score
            couch.user.couchinnuser.save()
            couch.save()
            req.save()
            return HttpResponseRedirect(reverse('lodgment:index'))
    return render(request, 'lodgment/score_couch.html', {'form': form,
                                                         'req':req})

@login_required
def score_host(request,request_id):
    form = ScoreForm(request.POST or None)
    req = get_object_or_404(Request, pk=request_id)
    if request.method == 'POST':
        if form.is_valid():
            score = form.cleaned_data['score']
            score = int(score)
            couchinnuser = req.author.couchinnuser
            couchinnuser.as_host_rank = couchinnuser.as_host_rank + score
            req.tenant_scored = True
            couchinnuser.save()
            req.save()
            return HttpResponseRedirect(reverse('lodgment:index'))
    return render(request, 'lodgment/score_host.html', {'form': form,
                                                        'req': req})
