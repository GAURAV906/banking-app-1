# Generated by Django 3.0.3 on 2020-02-23 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_transactions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='user',
        ),
    ]