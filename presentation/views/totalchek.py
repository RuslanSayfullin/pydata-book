from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework.generics import get_object_or_404
from json import loads, dumps
from appmain.models import Reckoning


@csrf_protect
def total_chek(request, reckoning_uuid):
    """Функционал, для заполнения итоговой таблицы. Данные из данной таблицы, будут распечатаны"""
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)

    specification = {}
    total_cost = {'total_price': 0, 'total_discounted_price': 0}

    for key in (x for x in range(1, 16)):
        specification[key] = {}
        specification[key]['spec_nomination'] = request.POST.get('spec_nomination_'+str(key)) if request.POST.get('spec_nomination_'+str(key)) else None
        specification[key]['spec_price'] = request.POST.get('spec_price_'+str(key)) if request.POST.get('spec_price_'+str(key)) else None
        specification[key]['spec_discounted_price'] = request.POST.get('spec_discounted_price_' + str(key)) if request.POST.get('spec_discounted_price_' + str(key)) else None

        total_cost[key] = specification[key]
        try:
            total_cost['total_price'] += int(specification[key]['spec_price'])
            total_cost['total_discounted_price'] += int(specification[key]['total_discounted_price'])
        except TypeError:
            continue

    if request.method == "POST":
        the_json = dumps(specification)
        reckoning.specification = the_json
        reckoning.total_price = total_cost['total_price']
        reckoning.total_discounted_price = total_cost['total_discounted_price']
        reckoning.save()
    else:
        try:
            the_dict = loads(reckoning.specification)
            for key in (x for x in range(1, 16)):
                specification[key] = the_dict[str(key)]
        except ValueError:
            pass

    return render(request, 'presentation/total_chek_create_update.html', {'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning, 'specification': specification, 'total_chek': True, })

