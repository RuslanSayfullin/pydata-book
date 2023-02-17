from django.views import generic
from presentation.forms import OfferpageForm


class CreateUpdateOfferpage(generic.FormView):
    """Создаём отдельную позицию для каждой единицы мебели в КП."""
    template_name = 'presentation/newreckoning/create_update.html'
    form_class = OfferpageForm
