from django.db import models
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    """Мероприятие"""

    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
    )
    content = models.TextField(
        max_length=20000,
        verbose_name='Контент',
    )
    preview_text = models.TextField(
        max_length=5000,
        verbose_name='Текст для главной превью',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    created_user = models.ForeignKey(
        'user.User',
        verbose_name='Создатель мероприятия',
        on_delete=models.CASCADE,
    )
    from_date = models.DateField(
        verbose_name='Дата начала мероприятия'
    )
    to_date = models.DateField(
        verbose_name='Дата окончания мероприятия'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Мероприятие')
        verbose_name_plural = _('Мероприятия')

