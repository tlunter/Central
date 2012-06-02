from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.channels.models import Channel, Message
from app.channels.views import serializers

def list_channels(request):
    channels = Channel.objects.all()

    return HttpResponse(serializers.serialize(channels, fields=('name',), use_natural_keys = True))

