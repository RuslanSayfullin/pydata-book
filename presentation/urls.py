from django.urls import re_path

from presentation import views


app_name = 'presentation'
urlpatterns = [
    re_path(r'^(?P<reckoning_uuid>\w+)$', views.CreateUpdateReckoning.as_view(), name="create_update"),
    re_path(r'^(?P<reckoning_uuid>\w+)/total_chek$', views.total_chek, name="total_chek"),
]