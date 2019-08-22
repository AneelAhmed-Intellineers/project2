# Generated by Django 2.2.4 on 2019-08-22 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190822_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='user_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_inbox', to='app.UserAccount'),
        ),
        migrations.AlterField(
            model_name='outbox',
            name='user_account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_outbox', to='app.UserAccount'),
        ),
    ]
