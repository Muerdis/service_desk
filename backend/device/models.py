from django.contrib.postgres.fields import JSONField
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    class Meta:
        verbose_name = _('Шаблон оборудования')
        verbose_name_plural = _('Шаблоны оборудования')


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

    class Meta:
        verbose_name = _('Оборудование')
        verbose_name_plural = _('Оборудование')


class Reservation(models.Model):
    """Бронирование/обслуживание"""

    device = models.ForeignKey(
        'device.Device',
        verbose_name='Оборудование',
        related_name='device_reservations',
        on_delete=models.CASCADE,
    )
    request = models.ForeignKey(
        'request.Request',
        verbose_name='Заявка',
        related_name='request_reservations',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    from_date = models.DateField(
        verbose_name='Дата начала бронирования/обслуживания'
    )
    to_date = models.DateField(
        verbose_name='Дата окончания бронирования/обслуживания'
    )

    def __str__(self):
        return '{} {} {}'.format(self.request.id if self.request else 'Обслуживание', self.device.name, self.device.inventory_number)

    class Meta:
        verbose_name = _('Бронирование/обслуживание')
        verbose_name_plural = _('Бронирование/обслуживание')
