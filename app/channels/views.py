from django.serializers import serializer
from django.http import HttpResponse

def get_channel(request, channel):
	channel = Channel.objects.get(name = channel)

	messages = channel.message_set

	sorted_messages = messages.order_by('-time_created')[0:50]

	return HttpResponse(serializer.serialize('json', sorted_messages))