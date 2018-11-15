from django.db import models


class RequestType(models.Model):
    """Тип заявки"""

    name = models.CharField(
        max_length=200,
        verbose_name='Название',
    )

    def __str__(self):
        return self.name


class Request(models.Model):
    """Заявка"""

    name = models.CharField(
        max_length=50,
        verbose_name='Название',
    )
    request_type = models.ForeignKey(
        'request.RequestType',
        verbose_name='Тип заявки',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'user.User',
        verbose_name='Владелец заявки',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
