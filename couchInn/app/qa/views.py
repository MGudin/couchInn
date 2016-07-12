from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.lodgment.models import Place
from app.session.models import CouchinnUser
from .forms import QuestionForm
from .models import Question


# Create your views here.

import pdb;
def ask(request, lodgment_id):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        lodgment = get_object_or_404(Place, pk=lodgment_id)
        question = form.save(commit=False)
        question.couch = lodgment
        question.user =request.user.couchinnuser
        question.save()
    else:
        request.session['post_data'] = request.POST
    return HttpResponseRedirect(reverse('lodgment:detail', args=(lodgment_id,)))
    
