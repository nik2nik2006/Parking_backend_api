# Generated by Django 5.0.2 on 2024-03-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
