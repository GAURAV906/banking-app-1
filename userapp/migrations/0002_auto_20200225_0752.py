# Generated by Django 3.0.3 on 2020-02-25 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='id',
            new_name='Transaction_Id',
        ),
    ]
