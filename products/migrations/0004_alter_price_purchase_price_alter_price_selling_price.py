# Generated by Django 5.1.7 on 2025-03-21 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_brand"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="purchase_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Цена закупки",
            ),
        ),
        migrations.AlterField(
            model_name="price",
            name="selling_price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Цена продажи",
            ),
        ),
    ]
