from django.contrib import admin

from staff.models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'departament')       # Поля, которые отображаются в панели администратора
    list_display_links = ('id', 'user')                         # Поля, которые открывают заявку в панели администратора
    search_fields = ('id', 'user')                              # Поля, по которым можно выполнять поиск
    list_filter = ('departament',)


admin.site.register(Staff, StaffAdmin)