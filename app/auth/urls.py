# These URLs are normally mapped to /admin/urls.py. This URLs file is
# provided as a convenience to those who want to deploy these URLs elsewhere.
# This file is also used to provide a reliable view deployment for test purposes.

from django.conf.urls.defaults import *

urlpatterns = patterns('app.auth.views',
	url(r'^profile/(?P<username>[^/]+)/$', 'profile', name = 'account-profile'),
	url(r'^profile/$', 'profile', name = 'account-profile'),
    url(r'^login/$', 'login', name = 'account-login'),
    url(r'^logout/$', 'logout', name = 'account-logout'),
#     (r'^login/$', 'app.auth.views.login'),
#     (r'^logout/$', 'app.auth.views.logout'),
#     (r'^password_change/$', 'app.auth.views.password_change'),
#     (r'^password_change/done/$', 'app.auth.views.password_change_done'),
#     (r'^password_reset/$', 'app.auth.views.password_reset'),
#     (r'^password_reset/done/$', 'app.auth.views.password_reset_done'),
#     (r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', 'app.auth.views.password_reset_confirm'),
#     (r'^reset/done/$', 'app.auth.views.password_reset_complete'),
)

