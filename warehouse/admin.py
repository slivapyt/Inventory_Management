from django.contrib import admin
from .models import Warehouse, Stock, Supplier, InternalMovement, MovementItem


@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
        "phone",
        "email",
    )
    list_filter = ("name",)
    search_fields = (
        "name",
        "address",
        "phone",
        "email",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "address",
                    "phone",
                    "email",
                ),
            },
        ),
    )


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "warehouse",
        "quantity",
        "unit",
        "expiration_date",
    )
    list_filter = (
        "warehouse",
        "product",
        "expiration_date",
    )
    search_fields = (
        "product__name",
        "warehouse_name",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "product",
                    "warehouse",
                    "quantity",
                    "unit",
                    "expiration_date",
                ),
            },
        ),
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "contact",
        "email",
        "phone",
    )
    list_filter = ("name",)
    search_fields = (
        "name",
        "contact",
        "email",
        "phone",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "contact",
                    "email",
                    "phone",
                ),
            },
        ),
    )


@admin.register(InternalMovement)
class InternalMovementAdmin(admin.ModelAdmin):
    list_display = (
        "from_warehouse",
        "to_warehouse",
        "date",
        "user",
        "comment",
    )
    list_filter = (
        "from_warehouse",
        "to_warehouse",
        "date",
        "user",
    )
    search_fields = (
        "from_warehouse__name",
        "to_warehouse__name",
        "user__username",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "from_warehouse",
                    "to_warehouse",
                    "date",
                    "user",
                    "comment",
                ),
            },
        ),
    )


@admin.register(MovementItem)
class MovementItemAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "quantity",
        "internal_movement",
    )
    list_filter = (
        "product",
        "internal_movement",
    )
    search_fields = (
        "product__name",
        "internal_movement__id",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "product",
                    "quantity",
                    "internal_movement",
                ),
            },
        ),
    )
