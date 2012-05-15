from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):

    return render_to_response('pages/index.html',
            {'title': 'Index',},
            context_instance = RequestContext(request))
