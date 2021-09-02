from django.contrib import admin
from .models import Story


# Register your models here.
class StoryAdmin(admin.ModelAdmin):
    list_display = (
        'Title', 'source', 'category', 'source_url', 'Datetime',
    )
    search_fields = (
        'source', 'category', 'Datetime',
    )
    readonly_fields = (
        'Title', 'source', 'category', 'source_url', 'Datetime', 'id',
    )
    ordering = ('Datetime',)

admin.site.register(Story, StoryAdmin)