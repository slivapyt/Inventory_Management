# Generated by Django 5.1.7 on 2025-03-20 08:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_rename_category_employeecategory_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employeecategory",
            options={
                "ordering": ["name"],
                "permissions": (
                    ("create_transfer", "Может создавать перемещения"),
                    ("accept_transfer", "Может принимать перемещения"),
                    ("accept_supply", "Может принимать поставки"),
                    ("create_inventory", "Может создавать инвентаризацию"),
                    ("confirm_inventory", "Может подтверждать инвентаризацию"),
                    ("create_write_off", "Может создавать списания на брак"),
                    ("confirm_write_off", "Может подтверждать списания на брак"),
                    ("edit_product", "Может редактировать товары"),
                    ("create_sale", "Может создавать продажи"),
                    ("cancel_sale", "Может отменять продажи"),
                    ("process_return", "Может обрабатывать возвраты"),
                    ("edit_supplier", "Может редактировать поставщиков"),
                    ("manage_users", "Может управлять пользователями"),
                    ("manage_roles", "Может управлять ролями и правами доступа"),
                ),
                "verbose_name": "Категория сотрудника",
                "verbose_name_plural": "Категории сотрудников",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="employee_id",
            field=models.PositiveIntegerField(
                blank=True, null=True, unique=True, verbose_name="ID сотрудника"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="employee_category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="users",
                to="users.employeecategory",
                verbose_name="Категория сотрудника",
            ),
        ),
    ]
