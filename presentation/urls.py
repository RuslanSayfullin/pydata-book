from django.urls import re_path

from presentation import views
from presentation.views.specification import specification_main_view

app_name = 'presentation'
urlpatterns = [
    re_path(r'^(?P<reckoning_uuid>\w+)/offer_pages$', views.createupdateofferpage, name="offer_pages"),

    re_path(r'^(?P<reckoning_uuid>\w+)/add_kitchen_offer_page$', views.addkitchenofferpage, name="add_kitchen_offer_page"),
    re_path(r'^(?P<reckoning_uuid>\w+)/kitchen_offerpages_list$', views.kitchen_offerpages_list, name='kitchen_offerpages_list'),
    re_path(r'^(?P<reckoning_uuid>\w+)/kitchen_count$', views.kitchen_count, name='kitchen_count'),
    re_path(r'^(?P<kitchenofferpage_id>\w+)/kitchen_offer_page_view$', views.kitchen_offer_page_view, name='kitchen_offer_page_view'),  # распечатать спецификацию



    re_path(r'^(?P<reckoning_uuid>\w+)/total_chek$', views.total_chek, name="total_chek"),
    re_path(r'^(?P<reckoning_uuid>\w+)/for_print$', specification_main_view, name='view'),  # распечатать спецификацию
]

