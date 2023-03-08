"""
Django admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from user import models


class UserAdmin(BaseUserAdmin):
    """Define user admin page"""
    ordering = ['id']
    list_display = ['id', 'name', 'email']

    fieldsets = [
        [None, {'fields': ['name', 'email', 'username']}],

        [
            _('Premissions'),
            {
                'fields': [
                    'is_active',
                    'is_staff',
                    'is_superuser'
                ]
            }
        ],
        [
            _('Important Dates'),
            {
                'fields': [
                    'last_login'
                ]
            }
        ]
    ]
    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)
