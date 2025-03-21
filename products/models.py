from config import settings

from django.core.validators import MinValueValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Supplier(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="Название поставщика",
    )
    contact = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Контактная информация",
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Электронная почта")
    phone = PhoneNumberField(blank=True, null=True, verbose_name="Телефон")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


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


class Stock(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name="stock",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name="Количество на складе",
        validators=[MinValueValidator(0)],
    )
    unit = models.CharField(
        max_length=50,
        default="шт",
        verbose_name="Единица измерения",
    )
    min_stock = models.PositiveIntegerField(
        default=1,
        verbose_name="Мин. остаток",
        validators=[MinValueValidator(0)],
    )
    max_stock = models.PositiveIntegerField(
        default=100,
        verbose_name="Макс. остаток",
        validators=[MinValueValidator(0)],
    )
    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Местоположение",
    )
    expiration_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Срок годности",
    )

    def __str__(self):
        return f"Остаток для {self.product.name}"

    class Meta:
        verbose_name = "Остаток"
        verbose_name_plural = "Остатки"


class Movement(models.Model):
    MOVEMENT_TYPES = [
        ("IN", "Приход"),
        ("OUT", "Расход"),
        ("MOVE", "Перемещение"),
    ]
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="movements",
    )
    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPES,
        verbose_name="Тип движения",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        validators=[MinValueValidator(1)],
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата движения")
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Пользователь",
    )

    def __str__(self):
        return f"{self.get_movement_type_display()} {self.quantity} {self.product.name}"

    class Meta:
        verbose_name = "Движение"
        verbose_name_plural = "Движения"
