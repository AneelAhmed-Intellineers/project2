# Generated by Django 2.2.3 on 2019-08-21 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190821_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='user',
        ),
        migrations.RemoveField(
            model_name='outbox',
            name='user',
        ),
    ]
