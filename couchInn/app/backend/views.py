# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Category
from forms import CategoryForm, DateFilterForm, RequestFilterForm
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Sum
from app.donation.models import Donation
from app.lodgment.models import Request
import datetime
# Create your views here.

@login_required
@permission_required('backend.add_category')
def new_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
       category = form.save(commit=False)
       category.save()
       return redirect(reverse('backend:home'))
    return render(request,'backend/new_category.html',{'form':form})

@login_required
@permission_required('backend.change_category')
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, instance = category)
    if form.is_valid():
       form.save()
       return redirect(reverse('backend:home'))
    return render(request,'backend/edit_category.html',{'form':form, 'category':category})
  
@login_required
def show_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request,'backend/show_category.html',{'category': category})

import pdb
@login_required

def home(request):
    categories = Category.objects.exclude(deleted=True)
    donation_filter_form = DateFilterForm(request.POST or None)
    request_filter_form = RequestFilterForm()
    requests = Request.objects.filter(state='AC')
    if request.method == 'POST':
        if donation_filter_form.is_valid():
            initial_date = request.POST['initial_date']
            initial_date = datetime.datetime.strptime(initial_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            finish_date = request.POST['finish_date']
            finish_date = datetime.datetime.strptime(finish_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            donations = Donation.objects.filter(donation_date__gte=initial_date).filter(donation_date__lte=finish_date)
        else:
            donations = Donation.objects.none()
    else:
        donations = Donation.objects.all()


    total_donations = donations.aggregate(Sum('amount'))
    return render(request,'backend/home.html',{'categories': categories,
                                               'donations' : donations,
                                               'donation_filter_form':donation_filter_form,
                                               'total_donations': total_donations['amount__sum'],
                                               'request_filter_form':request_filter_form,
                                               'requests':requests})


def request_filter(request):
    categories = Category.objects.exclude(deleted=True)
    donation_filter_form = DateFilterForm()
    donations = Donation.objects.all()
    total_donations = donations.aggregate(Sum('amount'))

    request_filter_form = RequestFilterForm(request.POST or None)

    if request.method == 'POST':
        if request_filter_form.is_valid():
            initial_date = request.POST['initial_date_s']
            initial_date = datetime.datetime.strptime(initial_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            finish_date = request.POST['finish_date_s']
            finish_date = datetime.datetime.strptime(finish_date, "%d/%m/%Y").strftime("%Y-%m-%d")
            requests = Request.objects.filter(state="AC").filter(date_accepted__gte=initial_date).filter(date_accepted__lte=finish_date)
        else:
            requests = Request.objects.none()
    else:
        requests = Request.objects.filter(state='AC')

    return render(request,'backend/home.html',{'categories': categories,
                                               'donations' : donations,
                                               'donation_filter_form':donation_filter_form,
                                               'total_donations': total_donations['amount__sum'],
                                               'requests':requests,
                                               'request_filter_form':request_filter_form})

    
    
@login_required
@permission_required('backend.delete_category')
def delete_category(request, category_id):
    u = get_object_or_404(Category, pk=category_id)
    if u.is_used():
        u.deleted=True
        u.save()
    else:
        u.delete()

    return HttpResponseRedirect(reverse('backend:home'))

