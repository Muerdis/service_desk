# Generated by Django 2.1.3 on 2019-06-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20190606_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='preview_text',
            field=models.TextField(default=None, max_length=5000, verbose_name='Текст для главной превью'),
            preserve_default=False,
        ),
    ]
