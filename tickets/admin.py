# infrabot_analytics_django/tickets/admin.py
from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model Ticket di dashboard admin Django.
    """
    list_display = ('ticket_id', 'vm_name', 'status', 'category', 'dev_ops', 'created_date', 'follow_up_date')
    list_filter = ('status', 'category', 'criticality', 'dev_ops')
    search_fields = ('ticket_id', 'vm_name', 'description')
    date_hierarchy = 'created_date'