# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .models import EmployeeCategory, Position, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name',
        'last_name', 'position', 'employee_id', 'employee_category', 'is_active',
    )
    list_filter = ('position', 'employee_category', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'email')}),
        ('Корпоративные данные пользователя', {'fields': ('position', 'employee_category', 'phone_number')}),
        (
            'Права',
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('username', 'email', 'password1', 'password2'),
            },
        ),
    )


@admin.register(EmployeeCategory)
class EmployeeCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    ordering = ('name',)
    filter_horizontal = ('permissions',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['permissions'].queryset = Permission.objects.filter(
            codename__in=[perm[0] for perm in EmployeeCategory._meta.permissions],
        )
        return form


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
