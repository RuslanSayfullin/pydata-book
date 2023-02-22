from django.contrib.auth.models import User
from django.db import models


class Reckoning(models.Model):
    uuid = models.CharField(editable=False, unique=True, max_length=40, db_index=True)
    designer = models.ForeignKey(User, related_name='froze_designer', on_delete=models.CASCADE, verbose_name="Дизайнер")
    client_data = models.CharField(max_length=100, verbose_name="Данные клиента")
    phone = models.CharField(max_length=50, verbose_name="Телефон Клиента")
    date = models.DateField(default=None, blank=True, null=True, verbose_name="Дата")
    specification = models.TextField(default='{"1": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "2": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "3": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "4": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "5": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "6": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "7": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "8": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "9": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "10": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "11": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "12": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "13": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "14": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}, "15": {"spec_nomination": null, "spec_price": null, "spec_discounted_price": null}}', blank=True, null=True)  # Спецификация (15 строк в табл.)
    total_price = models.PositiveIntegerField(default=None, blank=True, null=True)
    total_discounted_price = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.client_data

    class Meta:
        verbose_name = 'Просчёт'
        verbose_name_plural = 'Просчёты'


