# Generated by Django 5.0.2 on 2024-03-10 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0004_rename_is_available_parkingspace_is_works'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='is_purchased',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='rented_before',
        ),
        migrations.AddField(
            model_name='sale',
            name='rent_from',
            field=models.DateField(default=datetime.date(2024, 3, 10)),
        ),
        migrations.AddField(
            model_name='sale',
            name='rent_to',
            field=models.DateField(default=datetime.date(2024, 3, 10)),
        ),
    ]
