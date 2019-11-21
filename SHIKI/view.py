from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(req):
    return render_to_response('index2.html')

def info(req):
    return render_to_response('info.html')

def map_index(req):
    return render_to_response('map_index.html')

def tieba(req):
    return render_to_response('tieba_index.html')

def news_index(req):
    return render_to_response('news_index.html')


