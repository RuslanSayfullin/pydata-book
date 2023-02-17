from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404

from appmain.models import Reckoning
from presentation.forms import AddKitchenOfferpagePostForm


@csrf_protect
def createupdateofferpage(request, reckoning_uuid):
    """Создаём отдельную позицию для каждой единицы мебели в КП."""
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    return render(request, 'presentation/newreckoning/create_update.html', {'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning})


def addkitchenofferpage(request, reckoning_uuid):
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    if request.method == 'POST':
        form = AddKitchenOfferpagePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_update')
    else:
        form = AddKitchenOfferpagePostForm()
    return render(request, 'presentation/newreckoning/offerpages/addkitchen.html', {'form': form, 'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning})
