from django.contrib import admin

from appmain.models import Reckoning


class ReckoningAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'designer', 'client_data', 'phone')    # Поля, которые отображаются в панели администратора
    list_display_links = ('id', 'client_data')   # Поля, которые открывают заявку в панели администратора
    search_fields = ('id', 'uuid',)     # Поля, по которым можно выполнять пойск


admin.site.register(Reckoning, ReckoningAdmin)
