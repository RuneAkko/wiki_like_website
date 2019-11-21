from __future__ import  unicode_literals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from  map_manage.models import Domain, Topic, TopicRelation, AssembleText, Facet

def map(req):
    ctx = {}
    # ctx['title']
    ctx['domain'] = Domain.objects.all()
    ctx['type'] = 'map_manage'
    ctx['info1'] = "管理科学"
    ctx['info2'] = "是一门研究人类管理活动规律及其应用的科学。它偏重于用一些工具和方法来解决管理上的问题，如用运筹学、统计学等来定量定性分析"
    return render(req, 'map_classroot.html', ctx)
def map_topic(req, url):
    ctx= {}
    ctx['topic'] = Topic.objects.filter(classid=url).filter(ftopic_id=0)
    ctx['type'] = 'map_manage'
    ctx['info1'] = "管理科学"
    ctx['info2'] = "是一门研究人类管理活动规律及其应用的科学。它偏重于用一些工具和方法来解决管理上的问题，如用运筹学、统计学等来定量定性分析"
    # print(ctx['topic'])
    return render(req, 'map_classmiddle.html', ctx)
    # return HttpResponse('success')
def map_middle(req, url1, url3, url2):
    ctx2 = {}
    topicrelation = TopicRelation.objects.filter(parenttopicid=url2)
    if not topicrelation:
        try:
            pre_topic = TopicRelation.objects.get(childtopicid=url2)
        except:
            return HttpResponse("<title>该条目下暂无内容！</title><h1>该条目下暂无内容！</h1>")
        end_topic_id = pre_topic.childtopicid
        end_topic_name = pre_topic.childtopicname
        try:
            end_topic_facet = Facet.objects.filter(topicid=end_topic_id)
        except:
            return HttpResponse("<title>该条目下暂无内容！</title><h1>该条目下暂无内容！</h1>")
        ctx = {}
        for a in end_topic_facet:
            end_topic_facet_id = a.facetid
            text = AssembleText.objects.filter(facetid=end_topic_facet_id).filter(topicid=end_topic_id)
            text_sum = ""
            for b in text:
                text_sum = text_sum + b.textcontent
            ctx['text'] = text_sum

        ctx['end_topic_name'] = end_topic_name
        ctx['end_topic_facet'] = end_topic_facet
        if not end_topic_facet:
            ctx['abstract'] = "该条目下暂无内容！"
        else:
            ctx['abstract'] = end_topic_facet[0].facetlayer
        ctx['type'] = 'map_manage'
        ctx['info1'] = "管理科学"
        ctx['info2'] = "是一门研究人类管理活动规律及其应用的科学。它偏重于用一些工具和方法来解决管理上的问题，如用运筹学、统计学等来定量定性分析"
        return render(req, 'map_classend.html', ctx)
    else:
        ctx2['topic'] = topicrelation

        ctx2['type'] = 'map_manage'
        ctx2['info1'] = "管理科学"
        ctx2['info2'] = "是一门研究人类管理活动规律及其应用的科学。它偏重于用一些工具和方法来解决管理上的问题，如用运筹学、统计学等来定量定性分析"
        return render(req, 'map_classmiddle2.html', ctx2)