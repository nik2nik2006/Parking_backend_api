# Generated by Django 5.0.2 on 2024-03-09 21:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_available', models.BooleanField(default=True)),
                ('discount_parking', models.DecimalField(decimal_places=0, help_text='Скидка на парковочное место (от 0 до 99), проценты', max_digits=2)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('D', 'day'), ('M', 'month')], default='M', max_length=1)),
                ('amount', models.DecimalField(decimal_places=0, max_digits=6)),
                ('will_act', models.DateField(help_text='Начинает действовать с:')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rented_before', models.DateField()),
                ('promo_code', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=0, max_digits=16)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('is_purchased', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddConstraint(
            model_name='price',
            constraint=models.UniqueConstraint(fields=('name', 'will_act'), name='unique_price'),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='parking.price'),
        ),
        migrations.AddField(
            model_name='sale',
            name='parking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parking.parkingspace'),
        ),
    ]
