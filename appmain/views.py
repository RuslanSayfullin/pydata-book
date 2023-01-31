from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from appmain.models import Reckoning


def index(request):
    return render(request, 'appmain/index.html')


class ReckoningPermissionMixin(object):
    designer = None

    def get_designer(self):
        if self.designer:
            return self.designer

        username = self.kwargs.get("username", None)
        self.designer = get_object_or_404(User, username=username)
        return self.designer

    def dispatch(self, request, *args, **kwargs):
        designer = self.get_designer()
        username = request.user
        return super(ReckoningPermissionMixin, self).dispatch(request, *args, **kwargs)


class ReckoningDesignerView(ReckoningPermissionMixin, generic.ListView):
    template_name = 'appmain/reckoning_designer.html'
    context_object_name = "reckoning_items"

    def dispatch(self, *args, **kwargs):
        # <права доступа...
        return super(ReckoningDesignerView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ReckoningDesignerView, self).get_context_data(**kwargs)
        context["username"] = context["designer"] = self.get_designer()
        return context


class ReckoningView(ReckoningDesignerView):

    def get_reckoning(self):

        reckoning_items = Reckoning.objects.all()
        return reckoning_items

    def get_queryset(self):
        return self.get_reckoning()

    def get_context_data(self, **kwargs):
        context = super(ReckoningView, self).get_context_data(**kwargs)
        return context


