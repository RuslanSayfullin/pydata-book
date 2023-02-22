from django import template

from presentation.models import KitchenOfferpage

register = template.Library()


@register.simple_tag
def kitchen_offerpage_count(reckoning_uuid):
    return KitchenOfferpage.objects.filter(reckoning__uuid=reckoning_uuid).count()
