from django.contrib.auth.models import AbstractUser, Permission
from django.db import models

from users.user_permissions import USER_PERMISSIONS


optional_field = {'blank': True, 'null': True}


class User(AbstractUser):
    first_name = models.CharField(max_length=30, **optional_field, verbose_name='Имя')
    last_name = models.CharField(max_length=30, **optional_field, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=20, **optional_field, verbose_name='Телефон')
    email = models.EmailField(unique=True, verbose_name='Email')
    position = models.ForeignKey('Position', on_delete=models.SET_NULL,
                                 **optional_field, verbose_name='Должность')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 **optional_field, verbose_name='Категория',
                                 related_name='users')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f'{self.username}'


class Position(models.Model):
    title = models.CharField(max_length=100, verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, **optional_field,
                                 decimal_places=2, verbose_name='Оклад')
    responsibilities = models.TextField(verbose_name='Основные обязанности', **optional_field)

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['title']

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    permissions = models.ManyToManyField(Permission, blank=True, verbose_name='Права')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']
        permissions = USER_PERMISSIONS

    def __str__(self):
        return self.name
