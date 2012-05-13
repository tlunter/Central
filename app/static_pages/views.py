from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

def index(request):

    return render_to_response('static_pages/index.html',
            {},
            context_instance = RequestContext(request))
