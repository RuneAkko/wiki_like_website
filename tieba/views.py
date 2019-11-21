from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from tieba.models import Comment, Post, Thread
# Create your views here.
def tieba(req):
    return render(req, 'tieba_index.html')

def tieba_content(req,url):
    ctx = {}
    start = (int(url) - 1) * 50
    end = int(url) * 50
    pages = list(range(1, int(Post.objects.filter(floor=1).count() / 50) + 1))
    ctx['pages'] = pages[0:10]
    ctx['posts'] = Post.objects.filter(floor=1).order_by("-time")[start:end]
    return render(req, 'tieba_content.html', ctx)

def tieba_content2(req,url):
    ctx = {}
    ctx['posts'] = Post.objects.filter(thread_id=url).order_by("floor")
    ctx['num'] = url
    return render(req, 'tieba_content2.html',  ctx)


def tieba_content3(req,url):
    ctx = {}
    comments = Comment.objects.filter(post_id=url).order_by("id")
    ctx['comments'] = comments
    ctx['from'] = comments[0]

    return render(req, 'tieba_contentend.html', ctx)

def show(req):

    return render(req, 'picture_show_tieba.html')