from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('app.accounts.views',
	url(r'^profile/(?P<username>[^/]+)/$', 'profile', name = 'account-profile'),
	url(r'^profile/$', 'profile', name = 'account-profile'),
	url(r'^logout/$', 'logout', name = 'account-logout'),
	url(r'^login/$', 'login', name = 'account-login')
)