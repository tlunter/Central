from app.functions import full_title
from django import template

register = template.Library()

register.filter('full_title', full_title)