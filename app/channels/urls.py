from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.channels.views',
    url(r'^api/post-channel-message/(?P<channel>[^/]+)/$', 'post_channel.post_channel_message', name='post-channel-message'),
	url(r'^api/get-channel-messages/(?P<channel>[^/]+)/$', 'get_channel.get_channel_messages', name='get-channel-messages'),
    url(r'^api/get-channel-users/(?P<channel>[^/]+)/$', 'get_channel.get_channel_users', name='get-channel-users'),
    url(r'^api/list-channels/$', 'list_channels.list_channels', name='list-channels'),
)
