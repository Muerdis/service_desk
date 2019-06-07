from django.db import models
from djchoices import DjangoChoices, ChoiceItem
from django.utils.translation import gettext_lazy as _

from device.models import DeviceTemplate


class RequestReason(models.Model):
    """Причина заявки"""

    text = models.CharField(
        max_length=200,
        verbose_name='Текст',
        unique=True
    )
    request_type = models.ForeignKey(
        'request.RequestType',
        verbose_name='Тип заявки',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Причина заявки')
        verbose_name_plural = _('Причины заявки')


class RequestType(models.Model):
    """Тип заявки"""

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Тип заявки')
        verbose_name_plural = _('Типы заявок')


class RequestStatuses(DjangoChoices):
    """ Organization using
    """
    NEW = ChoiceItem(1, 'Новая')
    IN_WORK = ChoiceItem(2, 'В работе')
    CLOSED = ChoiceItem(3, 'Завершена')


class Request(models.Model):
    """Заявка"""

    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок',
        default=''
    )
    text = models.CharField(
        max_length=500,
        verbose_name='Текст',
        default=''
    )
    request_reason = models.ForeignKey(
        'request.RequestReason',
        verbose_name='Причина заявки',
        on_delete=models.CASCADE
    )
    assigned_user = models.ForeignKey(
        'user.User',
        verbose_name='На кого назначена заявка',
        related_name='assigned_user',
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время создания'
    )
    created_user = models.ForeignKey(
        'user.User',
        verbose_name='Создатель заявки',
        related_name='created_user',
        on_delete=models.CASCADE,
    )
    status = models.PositiveSmallIntegerField(
        verbose_name='Статус',
        choices=RequestStatuses.choices,
        default=RequestStatuses.NEW
    )
    device_templates = models.ManyToManyField(
        DeviceTemplate,
        verbose_name='Необходимое оборудование',
        blank=True, null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')


class Comment(models.Model):
    """Комментарий"""

    text = models.CharField(
        max_length=100,
        verbose_name='Текст',
    )
    request = models.ForeignKey(
        'request.Request',
        verbose_name='Заявка',
        on_delete=models.CASCADE
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    created_user = models.ForeignKey(
        'user.User',
        verbose_name='Создатель комментария',
        on_delete=models.CASCADE,
        related_name='request_comments'
    )

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.request.id,
            self.created_user.get_full_name(),
            self.date_created
        )

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
