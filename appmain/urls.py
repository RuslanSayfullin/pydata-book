from django.urls import path, re_path

from appmain.views import index, ReckoningView

urlpatterns = [
    path('', index, name='index'),
    re_path(r'^user/(?P<username>[-\w\.]+)/reckoning/$', ReckoningView.as_view(), name="reckoning_view"),
]
