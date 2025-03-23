from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings


from phonenumber_field.modelfields import PhoneNumberField


class Warehouse(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название склада",
    )
    address = models.TextField(
        blank=True,
        null=True,
        verbose_name="Адрес склада",
    )
    phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name="Телефон",
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Электронная почта объекта",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"


class Stock(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="stock",
        verbose_name="Товар",
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="stocks",
        verbose_name="Склад",
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
    expiration_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Срок годности",
    )

    def __str__(self):
        return f"Остаток для {self.product.name} на складе {self.warehouse}"

    class Meta:
        verbose_name = "Остаток"
        verbose_name_plural = "Остатки"
        unique_together = ("product", "warehouse")


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
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Электронная почта",
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Телефон",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"


class InternalMovement(models.Model):
    from_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="outgoing_movements",
        verbose_name="Склад отправитель",
    )
    to_warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="incoming_movements",
        verbose_name="Склад получатель",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата перемещения",
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Пользователь",
    )

    def __str__(self):
        return (
            f"Перемещение со склада {self.from_warehouse} на склад {self.to_warehouse}"
        )

    class Meta:
        verbose_name = "Внутреннее перемещение"
        verbose_name_plural = "Внутренние перемещения"


class MovementItem(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="movement_items",
        verbose_name="Товар",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество",
        validators=[MinValueValidator(1)],
    )
    internal_movement = models.ForeignKey(
        InternalMovement,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Внутреннее перемещение",
    )

    def __str__(self):
        return f"{self.quantity} {self.product.name}"

    class Meta:
        verbose_name = "Элемент перемещения"
        verbose_name_plural = "Элементы перемещения"
