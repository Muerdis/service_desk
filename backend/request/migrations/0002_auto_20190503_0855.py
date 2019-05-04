# Generated by Django 2.1.3 on 2019-05-03 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Название')),
                ('request_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.RequestType', verbose_name='Тип заявки')),
            ],
        ),
        migrations.RemoveField(
            model_name='request',
            name='name',
        ),
        migrations.RemoveField(
            model_name='request',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='request',
            name='request_type',
        ),
        migrations.AddField(
            model_name='request',
            name='assigned_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_user', to=settings.AUTH_USER_MODEL, verbose_name='На кого назначена заявка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='created_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL, verbose_name='Создатель заявки'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='date_created',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время создания'),
        ),
        migrations.AddField(
            model_name='request',
            name='device_templates',
            field=models.ManyToManyField(to='device.DeviceTemplate', verbose_name='Необходимое оборудование'),
        ),
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Новая'), (2, 'В работе'), (3, 'Завершена')], default=1, verbose_name='Статус'),
        ),
        migrations.AddField(
            model_name='request',
            name='text',
            field=models.CharField(default='', max_length=500, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='request',
            name='title',
            field=models.CharField(default='', max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='request',
            name='request_reason',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='request.RequestReason', verbose_name='Причина заявки'),
            preserve_default=False,
        ),
    ]
