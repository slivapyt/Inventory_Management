from django.core.validators import MinValueValidator
from django.db import models

from warehouse.models import Supplier


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Родительская категория",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название бренда")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    sku = models.CharField(max_length=100, unique=True, verbose_name="Артикул")
    barcode = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Штрихкод",
    )
    qr_code = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="QR-код",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Поставщик",
    )
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Фото",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Бренд",
    )

    def __str__(self):
        return f"{self.name} ({self.sku})"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Price(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="price",
    )
    purchase_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена закупки",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )
    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена продажи",
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
    )
    currency = models.CharField(max_length=3, default="RUB", verbose_name="Валюта")

    def __str__(self):
        return f"Цена для {self.product.name}"

    class Meta:
        verbose_name = "Цена"
        verbose_name_plural = "Цены"
