# Generated by Django 2.1.3 on 2019-05-18 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20190517_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invite_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время приглашения')),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашения',
            },
        ),
        migrations.CreateModel(
            name='VisitHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время посещения')),
                ('ip_address', models.CharField(max_length=100, verbose_name='IP адрес')),
            ],
            options={
                'verbose_name': 'История посещений',
                'verbose_name_plural': 'История посещений',
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='patronymic',
            new_name='middle_name',
        ),
        migrations.AddField(
            model_name='department',
            name='director',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='departments', to=settings.AUTH_USER_MODEL, verbose_name='Создатель комментария'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.Department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[user.validators.validate_phone], verbose_name='Номер мобильного телефона'),
        ),
        migrations.AddField(
            model_name='visithistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visit_histories', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='invite',
            name='invite_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to=settings.AUTH_USER_MODEL, verbose_name='Кто пригласил'),
        ),
        migrations.AddField(
            model_name='invite',
            name='invite_to',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Кого пригласили'),
        ),
    ]
