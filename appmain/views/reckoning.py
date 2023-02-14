import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.views import generic

from appmain.forms import NewReckoningForm
from appmain.models import Reckoning


def get_unique_uuid(model):
    while True:
        new_uuid = uuid.uuid4().hex
        try:
            model.objects.get(uuid=new_uuid)
        except ObjectDoesNotExist:
            return new_uuid


class NewReckoningView(generic.FormView):
    template_name = 'appmain/reckoning/new_reckoning.html'
    form_class = NewReckoningForm

    def form_valid(self, form):
        # <права доступа...
        reckoning_param = dict()
        reckoning_param['designer'] = form.cleaned_data['designer']
        reckoning_param['client_data'] = form.cleaned_data['client_data']
        reckoning_param['phone'] = form.cleaned_data['phone']
        reckoning_param['date'] = form.cleaned_data['date']
        reckoning = Reckoning(**reckoning_param)
        reckoning.uuid = get_unique_uuid(Reckoning)
        reckoning.save()

        self.designer = form.cleaned_data['designer']
        return super(NewReckoningView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs = super(NewReckoningView, self).get_context_data(**kwargs)
        kwargs["designer"] = self.request.GET.get('designer')
        return kwargs

    def get_initial(self):
        self.initial["designer"] = self.request.GET.get('designer')
        self.initial["client_data"] = self.request.GET.get('client_data') if self.request.GET.get('client_data') else ""
        self.initial["phone"] = self.request.GET.get('phone') if self.request.GET.get('phone') else ""
        self.initial["date"] = self.request.GET.get('date') if self.request.GET.get('date') else ""
        return super(NewReckoningView, self).get_initial()

    def get_success_url(self):
        username = self.designer
        return reverse_lazy("reckoning_view", kwargs={'username': username, })

