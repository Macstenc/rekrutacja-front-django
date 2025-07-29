from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'location', 'mode', 'organizer', 'capacity', 'registered']
    list_filter = ['mode', 'start_date']
    search_fields = ['name', 'description', 'location', 'organizer']
    readonly_fields = ['registered', 'created_at', 'updated_at']
    fieldsets = [
        (_('Event Information'), {'fields': ['name', 'description', 'start_date', 'end_date']}),
        (_('Location'), {'fields': ['location', 'mode']}),
        (_('Organization'), {'fields': ['organizer', 'color']}),
        (_('Capacity'), {'fields': ['capacity', 'registered']}),
        (_('Metadata'), {'fields': ['created_at', 'updated_at']}),
    ]

