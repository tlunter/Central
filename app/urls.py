from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),
	url(r'', include('auth.urls')),
    url(r'', include('pages.urls')),
    url(r'', include('channels.urls')),
    url(r'', include('client.urls')),
)
