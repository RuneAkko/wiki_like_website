from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from weibo.models import Post, User
from  django.db.models import Q
import re

# Create your views here.
def weibo(req):
    return render(req, "weibo_index.html")

def weibo_content(req,url):
    ctx = {}
    start = (int(url)-1)*50
    end = int(url)*50
    pages = list(range(1, int(Post.objects.count()/50) + 1))
    ctx['posts'] = Post.objects.all().order_by("-good_num")[start:end]
    ctx['pages'] = pages[0:10]
    return render(req, "weibo_content.html", ctx)

def weibo_contentend(req, url):
    ctx = {}
    try:
        ctx['users'] = User.objects.filter(
            Q(userid__contains=url)
        )[0]
        return render(req, "weibo_contentend.html", ctx)
    except:
        return HttpResponse("<h1>该博主信息暂无</h1>")

def show(req):
    return render(req, 'picture_show_weibo.html')

