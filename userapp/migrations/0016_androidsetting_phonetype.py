# Generated by Django 3.2.13 on 2022-04-27 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0015_signin'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidsetting',
            name='phoneType',
            field=models.CharField(blank=True, default='Andriod', max_length=128, null=True),
        ),
    ]
