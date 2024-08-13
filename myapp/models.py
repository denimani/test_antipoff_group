from django.db import models


class CadastralQuery(models.Model):
    cadastral_number = models.CharField(max_length=100, verbose_name="Кадастровый номер")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    response = models.BooleanField(blank=True, null=True, verbose_name="Ответ от внешнего сервера")
