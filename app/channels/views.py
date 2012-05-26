from django.core.serializers.json import Serializer
from django.utils.encoding import smart_unicode
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from app.channels.models import Channel, Message

class MySerializer(Serializer):
    def end_object(self, obj):
        self.objects.append(self._current)

        self._current = None

serializers = MySerializer()

def get_channel(request, channel, minimum = 0, maximum = 50):
    channel = get_object_or_404(Channel, name = channel)
    maximum = 50 if maximum > 50 else maximum
    minimum = 0 if minimum < 0 else minimum
    minimum = maximum - 1 if minimum >= maximum else minimum

    messages = channel.message_set.all()

    sorted_messages = messages.order_by('-time_created')[minimum:maximum]

    return HttpResponse(serializers.serialize(sorted_messages, fields=('time_created', 'message','channel','user'), use_natural_keys = True))

def get_channel_users(request, channel):
    channel = get_object_or_404(Channel, name = channel)

    users = channel.active_users.all()

    return HttpResponse(serializers.serialize(users, fields=('username','email',), use_natural_keys = True))

def list_channels(request):
    channels = Channel.objects.all()

    return HttpResponse(serializers.serialize(channels, fields=('name',), use_natural_keys = True))
