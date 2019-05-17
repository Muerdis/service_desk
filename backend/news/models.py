from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """Новость"""

    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
    )
    content = models.CharField(
        max_length=5000,
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


class Comment(models.Model):
    """Комментарий"""

    text = models.CharField(
        max_length=100,
        verbose_name='Текст',
    )
    news = models.ForeignKey(
        'news.News',
        verbose_name='Новость',
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
        related_name='news_comments'
    )

    def __str__(self):
        return '{0} {1} {2}'.format(
            self.news.title,
            self.created_user.get_full_name(),
            self.date_created
        )

    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
