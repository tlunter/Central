from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from app.auth.decorators import login_required
from app.channels.models import Channel

@login_required
def client(request, channel):
    channel = get_object_or_404(Channel, name = channel)
    
    return render_to_response('client/index.html',
        {
            'title': '"{0}" Channel'.format(channel.name),
            'channel': channel.name,
        },
        context_instance=RequestContext(request))
