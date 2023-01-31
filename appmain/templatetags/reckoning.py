from django import template
from django.contrib.auth import get_user_model

User = get_user_model()
register = template.Library()


@register.simple_tag()
def designer_item_sd():
    return User.objects.all().order_by('first_name')
