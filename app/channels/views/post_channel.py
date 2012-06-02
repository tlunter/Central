from django.conf import settings
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from app.channels.models import Channel, Message
from app.channels.views import serializers, get_channel

def post_channel_message(request, channel):
    if request.method != "POST":
        raise Http404

    if 'message' not in request.POST:
        raise Http404
    else:
        message = request.POST['message'].strip()
    
    if len(message) < settings.MESSAGE_LENGTH['min']:
        raise Http404

    if len(message) > settings.MESSAGE_LENGTH['max']:
        raise Http404

    minimum = request.POST['minimum'] if 'minimum' in request.POST else 0
    maximum = request.POST['maximum'] if 'maximum' in request.POST else  50
    
    final_message = Message.objects.create_message(user = request.user, message = message, channel = channel)

    return get_channel.get_channel_messages(request, channel, minimum, maximum)
