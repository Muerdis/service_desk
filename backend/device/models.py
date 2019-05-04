from django.contrib.postgres.fields import JSONField
from django.db import models


class DeviceTemplate(models.Model):
    """Шаблон оборудования"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        default=''
    )
    params = JSONField(verbose_name='Характеристики')

    def __str__(self):
        return self.name


class Device(models.Model):
    """Оборудование"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
        default=''
    )
    inventory_number = models.CharField(
        max_length=50,
        verbose_name='Инвентарный номер',
        unique=True
    )
    device_template = models.ForeignKey(
        'device.DeviceTemplate',
        verbose_name='Шаблон',
        related_name='device_template',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.inventory_number
