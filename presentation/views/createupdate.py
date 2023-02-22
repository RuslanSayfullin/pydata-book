from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
from json import loads, dumps

from appmain.models import Reckoning
from presentation.forms import AddKitchenOfferpageForm
from presentation.models import KitchenOfferpage


@csrf_protect
def createupdateofferpage(request, reckoning_uuid):
    """Создаём отдельную позицию для каждой единицы мебели в КП."""
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    return render(request, 'presentation/newreckoning/offer_pages.html', {'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning})


# Функционал для добавления отдельных позиций к КП
@login_required
def kitchen_offerpages_list(request, reckoning_uuid):
    """Список кухонных гарнитуров."""
    if request.method != "POST":
        form = AddKitchenOfferpageForm
    else:
        form = AddKitchenOfferpageForm(request.POST, request.FILES)
        if form.is_valid():
            form.reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
            new_form = form.save()
            new_form.save()
    kitchenofferpages = KitchenOfferpage.objects.filter(reckoning__uuid=reckoning_uuid).order_by('time_create').reverse()
    return render(request, 'presentation/newreckoning/offerpages/addkitchen_list.html', {'kitchenofferpages': kitchenofferpages, 'form': form, 'reckoning_uuid': reckoning_uuid})


def addkitchenofferpage(request, reckoning_uuid):
    """Добавить страницу к КП для кухонного гарнитура, к отдельным заявкам."""
    type_of_furniture = "Кухонный гарнитур"
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    if request.method != "POST":
        form = AddKitchenOfferpageForm
        return render(request, 'presentation/newreckoning/offerpages/addkitchen.html',
                      {'form': form, 'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning})
    else:
        form = AddKitchenOfferpageForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.reckoning = reckoning
            update_reckoning_specification(reckoning, new_form, type_of_furniture)
            new_form.save()
            return HttpResponseRedirect("offer_pages", {'reckoning_uuid': reckoning_uuid})


def update_reckoning_specification(reckoning, new_form, type_of_furniture):
    """Обновляем итоговую таблицу КП"""
    the_dict = loads(reckoning.specification)
    for key, value in the_dict.items():
        if the_dict[str(key)]['spec_nomination']:  # если spec_nomination != null
            continue
        else:
            the_dict[str(key)]['spec_nomination'] = type_of_furniture
            the_dict[str(key)]['spec_price'] = new_form.total_price
            the_dict[str(key)]['spec_discounted_price'] = new_form.total_discounted_price
            break
    the_json = dumps(the_dict)
    reckoning.specification = the_json
    reckoning.save()








