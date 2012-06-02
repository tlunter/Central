from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.channels.models import Channel, Message
from app.channels.views import serializers

def get_channel_users(request, channel):
    channel = get_object_or_404(Channel, name = channel)

    users = channel.active_users.all()

    return HttpResponse(serializers.serialize(users, fields=('username','email',), use_natural_keys = True))

