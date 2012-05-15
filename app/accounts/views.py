from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib.auth import logout as logout_fn
from app.accounts.models import User

def profile(request, username = None):
	if username is None and not request.user.is_authenticated():
		raise Http404()
			
	if username is None:
		username = request.user.username
	
	user = get_object_or_404(User, username = username)
	
	title = '{0}\'s Profile'.format(user.username)
	if user == request.user:
		title = 'Your Profile'
	
	return render_to_response('accounts/profile.html',
            {'user_profile': user,
             'title': title,},
            context_instance = RequestContext(request))
	
def login(request):
	from django.conf import settings
	return redirect(settings.LOGIN_URL)

@login_required
def logout(request):
	logout_fn(request)
	return redirect('index-page')
