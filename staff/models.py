from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Staff(models.Model):
    DEPARTAMENT_D = 0

    DEPARTAMENT_CHOICE = (
        (DEPARTAMENT_D, u"Дизайнеры"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Сотрудник")
    phone = models.CharField(f'Рабочий телефон', max_length=20, null=True, blank=True, help_text=f'используется в sms оповещения, формат 89123456789')
    departament = models.SmallIntegerField(choices=DEPARTAMENT_CHOICE, null=True, blank=True, verbose_name="Отдел")
    is_locking = models.BooleanField(default=False, help_text=f'Пользователь заблокирован на время, он можете входить, но не может получать новые замеры')

    class Meta:
        ordering = ("user",)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
