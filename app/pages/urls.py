from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.pages.views',
    url(r'^$', 'index', name = 'index-page'),
)
