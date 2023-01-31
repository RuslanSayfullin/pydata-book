from django.db import models


class Reckoning(models.Model):
    uuid = models.CharField(editable=False, unique=True, max_length=40, db_index=True)
    designer = models.CharField(max_length=100, verbose_name="Дизайнер")
    client_data = models.CharField(max_length=100, verbose_name="Данные клиента")
    phone = models.CharField(max_length=50, verbose_name="Телефон Клиента")
    date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.client_data

    class Meta:
        verbose_name = 'Просчёт'
        verbose_name_plural = 'Просчёты'
