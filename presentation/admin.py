from django.contrib import admin

from presentation.models import KitchenOfferpage


class KitchenOfferpageAdmin(admin.ModelAdmin):
    list_display = ('reckoning', 'time_create')    # Поля, которые отображаются в панели администратора
    list_display_links = ('reckoning', 'time_create')  # Поля, которые открывают заявку в панели администратора
    search_fields = ('reckoning', 'time_create')     # Поля, по которым можно выполнять пойск


admin.site.register(KitchenOfferpage, KitchenOfferpageAdmin)
