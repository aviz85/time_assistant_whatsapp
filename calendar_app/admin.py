from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start_datetime', 'end_datetime')
    search_fields = ('title', 'notes', 'user__username')
    list_filter = ('user', 'start_datetime', 'end_datetime')
