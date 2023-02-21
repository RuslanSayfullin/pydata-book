from django.urls import re_path

from presentation import views
from presentation.views.specification import specification_main_view

app_name = 'presentation'
urlpatterns = [
    re_path(r'^(?P<reckoning_uuid>\w+)/offerpages$', views.createupdateofferpage, name="create_update"),
    re_path(r'^addkitchenofferpage$', views.addkitchenofferpage, name="addkitchenofferpage"),

    re_path(r'^(?P<reckoning_uuid>\w+)/total_chek$', views.total_chek, name="total_chek"),
    re_path(r'^(?P<reckoning_uuid>\w+)/for_print$', specification_main_view, name='view'),  # распечатать спецификацию
]

