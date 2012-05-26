from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.channels.views',
	url(r'^api/get-channel/(?P<channel>[^/]+)/$', 'get_channel', name='get-channel'),
    url(r'^api/get-channel-users/(?P<channel>[^/]+)/$', 'get_channel_users', name='get-channel-users'),
    url(r'^api/list-channels/$', 'list_channels', name='list-channels'),
)
