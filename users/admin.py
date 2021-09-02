from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdministrator(UserAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'is_staff', 'is_active',
        'registration_date', 'last_login', 'is_staff', 'is_superuser',
    )
    search_fields = (
        'email', 'last_name', 'first_name', 'is_staff', 'is_supersuer',
    )
    readonly_fields = (
        'id', 'last_login',
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)

admin.site.register(User, UserAdministrator)