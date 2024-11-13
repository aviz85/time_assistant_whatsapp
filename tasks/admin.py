from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'priority', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'priority', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_editable = ('completed', 'priority')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ['completed', '-priority', '-created_at']
    date_hierarchy = 'created_at'
    list_per_page = 50

    fieldsets = (
        ('Task Info', {
            'fields': ('title', 'user', 'priority')
        }),
        ('Status', {
            'fields': ('completed',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
