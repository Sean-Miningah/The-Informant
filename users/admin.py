from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Comments

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

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment_content', 'last_modified',
    )
    ordering = ('date_created',)

admin.site.register(User,UserAdministrator)
admin.site.register(Comments,CommentAdmin)