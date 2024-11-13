from django.contrib import admin
from .models import Thread, Message

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    list_filter = ('user', 'created_at')
    search_fields = ('user__username',)
    date_hierarchy = 'created_at'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('thread', 'sender_type', 'ai_model', 'cost', 'created_at')
    list_filter = ('sender_type', 'ai_model', 'created_at')
    search_fields = ('content', 'thread__user__username')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
