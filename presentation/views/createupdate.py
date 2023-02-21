from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect, get_object_or_404

from appmain.models import Reckoning
from presentation.forms import AddKitchenOfferpagePostForm, AddKitchenOfferpageForm
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

    def get_context_data(self, **kwargs):
        context = super(AddKitchenView, self).get_context_data(**kwargs)
        self.reckoning_uuid = kwargs.get('reckoning_uuid')
        self.reckoning = get_object_or_404(Reckoning, uuid=self.reckoning_uuid)
        return context

    def dispatch(self, *args, **kwargs):
        self.reckoning_uuid = kwargs.get('reckoning_uuid')
        self.reckoning = get_object_or_404(Reckoning, uuid=self.reckoning_uuid)
        return super(AddKitchenView, self).dispatch(*args, **kwargs)

    def get_initial(self):
        self.initial["reckoning"] = self.reckoning
        self.initial["upperfacades"] = self.request.GET.get('upperfacades') if self.request.GET.get('upperfacades') else ""
        self.initial["lowerfacades"] = self.request.GET.get('lowerfacades') if self.request.GET.get('lowerfacades') else ""
        self.initial["tabletop"] = self.request.GET.get('tabletop') if self.request.GET.get('tabletop') else ""
        self.initial["other"] = self.request.GET.get('other') if self.request.GET.get('other') else ""
        self.initial["accessories"] = self.request.GET.get('accessories') if self.request.GET.get('accessories') else ""
        self.initial["total_price"] = self.request.GET.get('total_price') if self.request.GET.get('total_price') else ""
        self.initial["total_discounted_price"] = self.request.GET.get('total_discounted_price') if self.request.GET.get('total_discounted_price') else ""
        return super(AddKitchenView, self).get_initial()



    def form_valid(self, form):
        addkitchen_param = dict()
        addkitchen_param['reckoning'] = self.reckoning
        addkitchen_param['upperfacades'] = form.cleaned_data['upperfacades']
        addkitchen_param['lowerfacades'] = form.cleaned_data['lowerfacades']
        addkitchen_param['tabletop'] = form.cleaned_data['tabletop']
        addkitchen_param['other'] = form.cleaned_data['other']
        addkitchen_param['accessories'] = form.cleaned_data['accessories']
        addkitchen_param['total_price'] = form.cleaned_data['total_price']
        addkitchen_param['total_discounted_price'] = form.cleaned_data['total_discounted_price']
        kitchenofferpage = KitchenOfferpage(**addkitchen_param)
        kitchenofferpage.save()
        return super(AddKitchenView, self).form_valid(form)

    def get_success_url(self):
        reckoning_uuid = self.reckoning_uuid
        return reverse_lazy("create_update", kwargs={'reckoning_uuid': reckoning_uuid, })


def addkitchenofferpage(request):
    if request.method == 'POST':
        form = AddKitchenOfferpageForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                form.save()
                return redirect('appmain:index')
            except:
                form.add_error(None, 'Ошибка добавления позиций')
    else:
        form = AddKitchenOfferpageForm
    return render(request, 'presentation/newreckoning/offerpages/addkitchen.html', {'form': form})
