from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'', include('social_auth.urls')),
	url(r'', include('auth.urls')),
    url(r'', include('pages.urls')),
    url(r'', include('channels.urls')),
	
    # Examples:
    # url(r'^$', 'Central.views.home', name='home'),
    # url(r'^Central/', include('Central.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
