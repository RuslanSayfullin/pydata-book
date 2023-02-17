from django.db import models

from appmain.models import Reckoning


class Offerpage(models.Model):
    """Модель описывает каждую отдельную позиию в КП"""
    reckoning = models.ForeignKey(Reckoning, on_delete=models.CASCADE, verbose_name="Зявка")
