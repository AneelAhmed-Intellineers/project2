# Generated by Django 2.2.3 on 2019-08-21 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='inbox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inbox', to='app.Inbox'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='outbox',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outbox', to='app.Outbox'),
        ),
    ]
