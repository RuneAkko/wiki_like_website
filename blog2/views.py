from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from blog2.models import BlogDetail
import re
# Create your views here.
def blog(req):
    return render(req, "blog2.html")

def blog_content(req, url):
    ctx = {}
    start = (int(url) - 1) * 50
    end = int(url) * 50
    pages = list(range(1, int(BlogDetail.objects.count() / 50) + 1))
    blogs = BlogDetail.objects.all()[start:end]
    for e in blogs:
        content = re.sub(
        r'</?\w+[^>]*>|<br\s*?/?>|<!--[^>]*-->|<\s*script[^>]*>[^<]*<\s*/\s*script\s*>|<\s*style[^>]*>[^<]*<\s*/\s*style\s*>|\r|\n|\t',
        "", e.blog_content)
        title = re.sub(r'<h6 class="title-article">|</h6>', "", e.title)
        views = re.sub(r'<span class="read-count">|</span>', "",
                       e.viewtime)
        comment = re.sub(r'<span class="read-num">|</span>', "", e.comment_num)
        e.comment_num = comment
        e.blog_content = content
        e.title = title
        e.viewtime = views
        e.save()
    #     types.add(tag)
    # for e in types:
    #     temp = Articles.objects.filter(tags=e)
    #     ctx['e'] = temp
    # ctx['tag'] = types
    ctx['pages'] = pages[0:10]
    ctx['blog'] = blogs
    return render(req, "blog2_content.html", ctx)
# Create your views here.
def blog_contentend(req, url1):
    print(url1)
    # print(url1)
    ctx = {}
    try:
        blogs = BlogDetail.objects.get(title=url1)
        ctx['blog'] = blogs
        return render(req, "blog2_contentend.html", ctx)
    except:
        return HttpResponse("<h1>博文暂无</h1>")