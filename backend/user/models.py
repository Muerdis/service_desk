from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.validators import validate_phone


class User(AbstractUser):
    """Пользователь"""

    patronymic = models.CharField(
        'Отчество',
        max_length=100,
        null=True,
        blank=True
    )
    phone = models.CharField(
        'Номер мобильного телефона',
        max_length=10,
        null=True,
        blank=True,
        validators=[validate_phone]
    )
    is_verify_phone = models.BooleanField(
        'Телефон подтвержден',
        default=False
    )
    is_verify_email = models.BooleanField(
        'Почта подтверждена',
        default=False
    )
    department = models.ForeignKey(
        'user.Department',
        verbose_name='Отдел',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def get_full_name(self):
        return '{0}{1}{2}'.format(
            '%s ' % self.last_name or '',
            '%s ' % self.first_name or '',
            '%s' % self.patronymic or ''
        )

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')


class Department(models.Model):
    """Отдел"""

    name = models.CharField(
        max_length=100,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Отдел')
        verbose_name_plural = _('Отделы')
