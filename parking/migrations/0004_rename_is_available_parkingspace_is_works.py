# Generated by Django 5.0.2 on 2024-03-10 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_remove_parkingspace_price_alter_sale_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parkingspace',
            old_name='is_available',
            new_name='is_works',
        ),
    ]