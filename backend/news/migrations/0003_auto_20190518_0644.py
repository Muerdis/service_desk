# Generated by Django 2.1.3 on 2019-05-18 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190517_1936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_user',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='news',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
