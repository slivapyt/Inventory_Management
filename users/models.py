from django.contrib.auth.models import AbstractUser
from django.db import models


optional_field = {'blank': True, 'null': True}


class User(AbstractUser):
    first_name = models.CharField(max_length=30, **optional_field, verbose_name='Имя')
    last_name = models.CharField(max_length=30, **optional_field, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, **optional_field, verbose_name='Телефон')
    email = models.EmailField(unique=True, **optional_field, verbose_name='Email')
    job = models.ForeignKey('Job', on_delete=models.SET_NULL,
                            **optional_field, verbose_name='Должность')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 **optional_field, verbose_name='Категория',
                                 related_name='users')

    def __str__(self):
        return f'{self.username}'


class Job(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')

    create_transfer = models.BooleanField(default=False, verbose_name='Создание перемещений')
    accept_transfer = models.BooleanField(default=False, verbose_name='Приём перемещений')

    accept_supply = models.BooleanField(default=False, verbose_name='Приём поставок')

    create_inventory = models.BooleanField(default=False, verbose_name='Создание инвентаризации')
    confirm_inventory = models.BooleanField(default=False,
                                            verbose_name='Подтверждение инвентаризации')

    create_write_off = models.BooleanField(default=False, verbose_name='Создание списания на брак')
    confirm_write_off = models.BooleanField(default=False,
                                            verbose_name='Подтверждение списания на брак')

    edit_product = models.BooleanField(default=False, verbose_name='Редактирование товаров')

    create_sale = models.BooleanField(default=False, verbose_name='Создание продаж')
    cancel_sale = models.BooleanField(default=False, verbose_name='Отмена продаж')
    process_return = models.BooleanField(default=False, verbose_name='Обработка возвратов')

    edit_supplier = models.BooleanField(default=False, verbose_name='Редактирование поставщиков')

    manage_users = models.BooleanField(default=False, verbose_name='Управление пользователями')
    manage_roles = models.BooleanField(default=False,
                                       verbose_name='Управление ролями и правами доступа')

    def __str__(self):
        return self.name
