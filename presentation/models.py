from django.db import models

from appmain.models import Reckoning


class KitchenOfferpage(models.Model):
    """Модель описывает каждую отдельную позиию в КП"""
    reckoning = models.ForeignKey(Reckoning, on_delete=models.CASCADE, verbose_name="Коммерческое предложение")
    upperfacades = models.CharField(max_length=250, verbose_name="Фасады (верх)")
    lowerfacades = models.CharField(max_length=250, verbose_name="Фасады (низ)")
    tabletop = models.CharField(max_length=250, verbose_name="Столешница")
    other = models.CharField(max_length=250, verbose_name="Прочее")
    accessories = models.CharField(max_length=250, verbose_name="Фурнитура")
    sketch = models.ImageField(upload_to="sketch/%Y/%m/%d/", verbose_name="Эскиз")
    costcalculation = models.FileField(upload_to='costcalculation/%Y/%m/%d/')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = 'КП для кухни'
        verbose_name_plural = 'КП для кухонь'
