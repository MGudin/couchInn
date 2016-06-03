# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Category
from forms import CategoryForm
from django.contrib.auth.decorators import login_required, permission_required 
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

@login_required
def home(request):
    categories = Category.objects.exclude(deleted=True)
    return render(request,'backend/home.html',{'categories': categories})

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
