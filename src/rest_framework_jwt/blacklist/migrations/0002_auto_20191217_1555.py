# Generated by Django 2.2.5 on 2019-12-17 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blacklist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklistedtoken',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blacklistedtoken',
            name='expires_at',
        ),
    ]
