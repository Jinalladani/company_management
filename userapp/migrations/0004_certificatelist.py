# Generated by Django 3.2.13 on 2022-04-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_companylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificateList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateName', models.CharField(blank=True, max_length=128, null=True)),
                ('client_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userapp.client')),
            ],
        ),
    ]
