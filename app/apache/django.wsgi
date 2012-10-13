import os, sys
import site

site.addsitedir('/home/tlunter/Envs/Central/lib/python2.7/site-packages/')

APACHE_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECTS_PATH = os.path.abspath(os.path.dirname(APACHE_PATH))
PROJECT_NAME = os.path.split(PROJECTS_PATH)[-1]
ROOT_PATH = os.path.abspath(os.path.dirname(PROJECTS_PATH))

sys.path.append(APACHE_PATH)
sys.path.append(PROJECTS_PATH)
sys.path.append(ROOT_PATH)

os.environ['DJANGO_SETTINGS_MODULE'] = PROJECT_NAME + '.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
