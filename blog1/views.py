from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog1.models import Articles
import re

def blog(req):
    return render(req, "blog1.html")

def blog_content(req,url):
    ctx = {}
    start = (int(url) - 1) * 50
    end = int(url) * 50
    pages = list(range(1, int(Articles.objects.count() / 50) + 1))
    blogs = Articles.objects.all()[start:end]
    # types = set()
    for e in blogs:
        tag = e.tags.split('|')[0].replace(' ', "")
        content = re.sub(
        r'</?\w+[^>]*>|<br\s*?/?>|<!--[^>]*-->|<\s*script[^>]*>[^<]*<\s*/\s*script\s*>|<\s*style[^>]*>[^<]*<\s*/\s*style\s*>|\r|\n|\t',
        "", e.content)
        e.tags = tag
        e.content = content
        e.save()
    #     types.add(tag)
    # for e in types:
    #     temp = Articles.objects.filter(tags=e)
    #     ctx['e'] = temp
    # ctx['tag'] = types
    ctx['blog'] = blogs
    ctx['pages'] = pages[0:10]
    return render(req, "blog1_content.html", ctx)
# Create your views here.
def blog_contentend(req, url1):
    print(url1)
    # print(url1)
    ctx = {}
    try:
        blogs = Articles.objects.get(url_object_id=url1)
        ctx['blog'] = blogs
        return render(req, "blog1_contentend.html", ctx)
    except:
        return HttpResponse("<h1>博文暂无</h1>")