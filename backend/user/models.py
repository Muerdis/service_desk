from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from user.validators import validate_phone


class User(AbstractUser):
    """Пользователь"""

    middle_name = models.CharField(
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
        validators=[validate_phone],
        unique=True
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
        on_delete=models.CASCADE,
        related_name='users'
    )

    def get_full_name(self):
        return '{0}{1}{2}'.format(
            '%s ' % self.last_name or '',
            '%s ' % self.first_name or '',
            '%s' % self.middle_name or ''
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
        unique=True
    )
    director = models.ForeignKey(
        'user.User',
        verbose_name='Создатель комментария',
        on_delete=models.CASCADE,
        related_name='departments'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Отдел')
        verbose_name_plural = _('Отделы')


class Invite(models.Model):
    """Приглашение"""

    invite_from = models.ForeignKey(
        'user.User',
        verbose_name='Кто пригласил',
        on_delete=models.CASCADE,
        related_name='invites'
    )
    invite_to = models.OneToOneField(
        'user.User',
        verbose_name='Кого пригласили',
        on_delete=models.CASCADE,
        unique=True
    )
    invite_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время приглашения'
    )

    def __str__(self):
        return self.invite_to.email

    class Meta:
        verbose_name = _('Приглашение')
        verbose_name_plural = _('Приглашения')


class VisitHistory(models.Model):
    """История посещений"""

    user = models.ForeignKey(
        'user.User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='visit_histories'
    )
    visit_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время посещения'
    )
    ip_address = models.CharField(
        max_length=100,
        verbose_name='IP адрес'
    )

    def __str__(self):
        return '{0} {1}'.format(self.visit_date, self.user.email)

    class Meta:
        verbose_name = _('История посещений')
        verbose_name_plural = _('История посещений')
