from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.channels.views',
	url(r'^get_channel/(?P<channel>[^/]+)/$', 'get_channel', name='get-channel'),
)