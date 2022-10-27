"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['username', 'first_name', 'last_name', 'user_group']
    fieldsets = (
        (_('User'), {'fields': ('username', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                )
            }

        ),
        (_('Important dates'), {'fields': ('last_login', )}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'user_group',
                'is_active',
                'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
