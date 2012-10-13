from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('app.client.views',
    url(r'^client/(?P<channel>[^/]+)/$', 'client', name = 'client-page'),
)
