# Generated by Django 3.2.13 on 2022-04-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0019_remove_notifactionsetting_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notifactionsetting',
            name='nList',
        ),
        migrations.AddField(
            model_name='notifactionsetting',
            name='defaultTime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='notifactionsetting',
            name='emailService',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notifactionsetting',
            name='fcmService',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notifactionsetting',
            name='smsService',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notifactionsetting',
            name='voiceNotiService',
            field=models.BooleanField(default=False),
        ),
    ]
