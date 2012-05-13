from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.static_pages.views',
    url(r'^$', 'index', name = 'index-page'),
)
