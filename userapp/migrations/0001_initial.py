# Generated by Django 3.0.3 on 2020-02-20 09:02

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('dob', models.DateField(max_length=8)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid5, editable=False, primary_key=True, serialize=False)),
                ('acc_no', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('min_bal', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User')),
            ],
        ),
    ]