#-*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
#, get_object_or_404
from django.template import RequestContext


def home(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
