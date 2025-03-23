from django.contrib import admin
from .models import Product, Price, Category, Brand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "sku",
        "barcode",
        "category",
        "supplier",
    )
    list_filter = (
        "category",
        "brand",
        "supplier",
    )
    search_fields = (
        "name",
        "brand",
        "sku",
        "barcode",
    )
    readonly_fields = ()
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "brand",
                    "sku",
                    "barcode",
                    "qr_code",
                    "category",
                    "supplier",
                ),
            },
        ),
        (
            "Дополнительная информация",
            {
                "fields": (
                    "description",
                    "image",
                ),
            },
        ),
    )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "purchase_price",
        "selling_price",
        "currency",
    )
    list_filter = ("currency",)
    search_fields = ("product__name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
    )
    search_fields = ("name",)
    list_filter = ("parent",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "parent",
                ),
            },
        ),
    )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
