from django import template
from django.contrib.auth import get_user_model

from staff.models import Staff

User = get_user_model()
register = template.Library()


@register.simple_tag()
def designer_item_d():
    return User.objects.filter(staff__departament=Staff.DEPARTAMENT_D, is_active=True).order_by('first_name')
