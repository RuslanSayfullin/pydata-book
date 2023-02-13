from django.views import generic
from presentation.forms import DogovorForm


class CreateUpdateReckoning(generic.FormView):
    template_name = 'newreckoning/create_update.html'
    form_class = DogovorForm
