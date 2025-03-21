from django.contrib import admin
from .models import Product, Price, Supplier, Category, Brand, Stock, Movement


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "brand", "sku", "barcode", "category", "supplier")
    list_filter = ("category", "brand", "supplier")
    search_fields = ("name", "brand", "sku", "barcode")
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
        ("Дополнительная информация", {"fields": ("description", "image")}),
    )


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("product", "purchase_price", "selling_price", "currency")
    list_filter = ("currency",)
    search_fields = ("product__name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "email", "phone")
    search_fields = ("name", "contact", "email", "phone")
    list_filter = ("name",)
    fieldsets = ((None, {"fields": ("name", "contact", "email", "phone")}),)
    add_fieldsets = ((None, {"fields": ("name", "contact", "email", "phone")}),)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent")
    search_fields = ("name",)
    list_filter = ("parent",)
    fieldsets = ((None, {"fields": ("name", "parent")}),)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "unit",
        "min_stock",
        "max_stock",
        "location",
        "expiration_date",
    )

    list_filter = ("unit", "location", "expiration_date")
    search_fields = ("product__name", "location")
    list_editable = ("quantity", "min_stock", "max_stock", "location")
    fieldsets = (
        (None, {"fields": ("product", "quantity", "unit", "min_stock", "max_stock")}),
        (
            "Дополнительная информация",
            {"fields": ("location", "expiration_date"), "classes": ("collapse",)},
        ),
    )


@admin.register(Movement)
class MovementAdmin(admin.ModelAdmin):
    list_display = ("product", "movement_type", "quantity", "date", "user")
    list_filter = ("movement_type", "date", "user")
    search_fields = ("product__name", "comment")
    date_hierarchy = "date"
    ordering = ("-date",)
