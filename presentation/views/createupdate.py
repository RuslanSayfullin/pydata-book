from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404

from appmain.models import Reckoning
from presentation.forms import AddKitchenOfferpagePostForm
from presentation.models import KitchenOfferpage


@csrf_protect
def createupdateofferpage(request, reckoning_uuid):
    """Создаём отдельную позицию для каждой единицы мебели в КП."""
    reckoning = get_object_or_404(Reckoning, uuid=reckoning_uuid)
    return render(request, 'presentation/newreckoning/create_update.html', {'reckoning_uuid': reckoning_uuid, 'reckoning': reckoning})


class AddKitchenView(generic.FormView):
    template_name = 'presentation/newreckoning/offerpages/addkitchen.html'
    form_class = AddKitchenOfferpagePostForm
    reckoning = None
    reckoning_uuid = None
    kitchenofferpage = None

    def get_context_data(self, **kwargs):
        context = super(AddKitchenView, self).get_context_data(**kwargs)
        context.update({
            'reckoning_uuid': self.kwargs.get('reckoning_uuid'),
            'reckoning': self.reckoning,
            'kitchenofferpage': self. kitchenofferpage,
        })
        return context

    def dispatch(self, *args, **kwargs):
        self.reckoning_uuid = kwargs.get('reckoning_uuid')
        self.reckoning = get_object_or_404(Reckoning, uuid=self.reckoning_uuid)
        try:
            self.kitchenofferpage = KitchenOfferpage.objects.get(reckoning_id=self.reckoning)
        except ObjectDoesNotExist:
            pass
        return super(AddKitchenView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        pass





def addkitchenofferpage(request, reckoning_uuid):
    if request.method == 'POST':
        form = AddKitchenOfferpagePostForm(request.POST, request.FILES)
        if form.is_valid():

            try:
                KitchenOfferpage.objects.create(**form.cleaned_data)
                return redirect('presentation:create_update')
            except:
                form.add_error(None, 'Ошибка добавления')
    else:
        form = AddKitchenOfferpagePostForm()
    return render(request, 'presentation/newreckoning/offerpages/addkitchen.html', {'form': form, 'reckoning_uuid': reckoning_uuid, })
