from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from models import Category
from forms import CategoryForm
# Create your views here.

def new_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
       category = form.save(commit=False)
       category.save()
       return redirect(reverse('backend:home'))
    return render(request,'backend/new_category.html',{'form':form})

def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    form = CategoryForm(request.POST or None, instance = category)
    if form.is_valid():
       form.save()
       return redirect(reverse('backend:home'))
    return render(request,'backend/edit_category.html',{'form':form, 'category':category})
  
def show_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request,'backend/show_category.html',{'category': category})

def home(request):
    categories = Category.objects.all()
    return render(request,'backend/home.html',{'categories': categories})

def delete_category(request, category_id):
    u = get_object_or_404(Category, pk=category_id).delete()
    return HttpResponseRedirect(reverse('backend:home'))
