from django.shortcuts import get_object_or_404

from appmain.models import Reckoning
from json import loads, dumps
from django.shortcuts import render


def specification_main_view(request, reckoning_uuid):
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    template = 'presentation/specification/specification.html'

    # Спецификация
    specification_chek = None
    sravn = '{' \
            '"1": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"2": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"3": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"4": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"5": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"6": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"7": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"8": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"9": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"10": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"11": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"12": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"13": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"14": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '"15": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, ' \
            '}'
    if reckoning.specification and reckoning.specification != sravn:
        try:
            specification_chek = {}
            the_dict = loads(reckoning.specification)

            for key in (x for x in range(1, 16)):
                if not the_dict[str(key)]['spec_nomination']:   # если spec_nomination == null
                    continue
                else:
                    specification_chek[key] = the_dict[str(key)]
        except ValueError:
            specification_chek = {'don_t_print': True}
    else:
        specification_chek = {'don_t_print': True}

    return render(request, template, {
        'reckoning': reckoning,
        'specification_chek': specification_chek,
    })





