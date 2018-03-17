# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    check = 'attempts' in request.session
    if check == False:
        request.session['attempts'] = 0
    else:
        request.session['attempts'] += 1
    context = {
        'attempts' : request.session['attempts']
    }
    return render(request, "random_word/index.html", context)

def create(request):
    if request.method == "POST":
        request.session['random_str'] = get_random_string(length=14)
        print(request.session['random_str'])
    return redirect('/')

def delete(request):
    if request.method == "POST":
        print('in delete route')
        del request.session['attempts']
    return redirect('/')