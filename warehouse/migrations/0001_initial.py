# Generated by Django 5.1.7 on 2025-03-23 10:28

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0005_remove_movement_product_remove_movement_user_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Supplier",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название поставщика"
                    ),
                ),
                (
                    "contact",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Контактная информация",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Электронная почта",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Телефон"
                    ),
                ),
            ],
            options={
                "verbose_name": "Поставщик",
                "verbose_name_plural": "Поставщики",
            },
        ),
        migrations.CreateModel(
            name="Warehouse",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название склада"),
                ),
                (
                    "address",
                    models.TextField(
                        blank=True, null=True, verbose_name="Адрес склада"
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True,
                        max_length=128,
                        null=True,
                        region=None,
                        verbose_name="Телефон",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="Электронная почта объекта",
                    ),
                ),
            ],
            options={
                "verbose_name": "Склад",
                "verbose_name_plural": "Склады",
            },
        ),
        migrations.CreateModel(
            name="InternalMovement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата перемещения"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
                (
                    "from_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outgoing_movements",
                        to="warehouse.warehouse",
                        verbose_name="Склад отправитель",
                    ),
                ),
                (
                    "to_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incoming_movements",
                        to="warehouse.warehouse",
                        verbose_name="Склад получатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Внутреннее перемещение",
                "verbose_name_plural": "Внутренние перемещения",
            },
        ),
        migrations.CreateModel(
            name="MovementItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="Количество",
                    ),
                ),
                (
                    "internal_movement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="warehouse.internalmovement",
                        verbose_name="Внутреннее перемещение",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="movement_items",
                        to="products.product",
                        verbose_name="Товар",
                    ),
                ),
            ],
            options={
                "verbose_name": "Элемент перемещения",
                "verbose_name_plural": "Элементы перемещения",
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "quantity",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                        verbose_name="Количество на складе",
                    ),
                ),
                (
                    "unit",
                    models.CharField(
                        default="шт", max_length=50, verbose_name="Единица измерения"
                    ),
                ),
                (
                    "expiration_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="Срок годности"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stock",
                        to="products.product",
                        verbose_name="Товар",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stocks",
                        to="warehouse.warehouse",
                        verbose_name="Склад",
                    ),
                ),
            ],
            options={
                "verbose_name": "Остаток",
                "verbose_name_plural": "Остатки",
                "unique_together": {("product", "warehouse")},
            },
        ),
    ]
