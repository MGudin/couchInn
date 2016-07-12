from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from app.lodgment.models import Place
from app.session.models import CouchinnUser
from .forms import QuestionForm, AnswerForm
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
    

def answer(request, question_id):
    form = AnswerForm(request.POST or None)
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user.couchinnuser
            answer.question = question
            answer.save()
            lodgment_id = question.couch.id
            return HttpResponseRedirect(reverse('lodgment:detail', args=(lodgment_id,)))
    return render(request, 'qa/answer.html', { 'form' : form, 'question': question})

    
