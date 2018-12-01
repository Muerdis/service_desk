from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class RequestReason(models.Model):
    """Причина заявки"""

    text = models.CharField(
        max_length=200,
        verbose_name='Название',
    )
    request_type = models.ForeignKey(
        'request.RequestType',
        verbose_name='Тип заявки',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.text


class RequestType(models.Model):
    """Тип заявки"""

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name


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
        max_length=200,
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

    def __str__(self):
        return self.title
