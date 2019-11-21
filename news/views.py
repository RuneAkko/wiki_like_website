from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from news.models import News2

# Create your views here.
def news(req):
    # ctx = {}
    # ctx['news'] =
    return render(req, "news.html")

def news_content(req, url):
    ctx = { }
    start = (int(url)-1)*50
    end = int(url)*50
    pages = list(range(1, int(News2.objects.count()/50)+1))
    ctx["news"] = News2.objects.order_by("-datetime")[start:end]
    ctx["pages"] = pages[0:10]
    return render(req, "news_content.html", ctx)

def picture_show(req):
    # ctx = {}ctx
    return render(req, "picture_show.html")
    # pass
