# Generated by Django 2.1.3 on 2019-06-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20190606_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='preview_text',
            field=models.TextField(default=None, max_length=5000, verbose_name='Текст для главной превью'),
            preserve_default=False,
        ),
    ]
