from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """Новость"""

    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
    )

    content = models.TextField(
        max_length=20000,
        verbose_name='Контент',
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    created_user = models.ForeignKey(
        'user.User',
        verbose_name='Создатель новости',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Новость')
        verbose_name_plural = _('Новости')
