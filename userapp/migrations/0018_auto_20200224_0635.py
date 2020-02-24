# Generated by Django 3.0.3 on 2020-02-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_deposit_withdraw'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Deposit',
        ),
        migrations.DeleteModel(
            name='Withdraw',
        ),
        migrations.AddField(
            model_name='transactions',
            name='action',
            field=models.CharField(default='deposit', max_length=8),
        ),
    ]