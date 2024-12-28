# Generated by Django 5.1.2 on 2024-10-19 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='customer',
            index=models.Index(fields=['last_naem', 'first_name'], name='store_custo_last_na_9d8241_idx'),
        ),
        migrations.AlterModelTable(
            name='customer',
            table='store_customer',
        ),
    ]
