# infrabot_analytics_django/datastores/admin.py
from django.contrib import admin
from .models import Datastore, StorageHistoricalLog # Import Model yang sudah dibuat

@admin.register(Datastore)
class DatastoreAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model Datastore di dashboard admin Django.
    """
    list_display = ('name', 'cluster', 'ds_type', 'capacity_gb', 'provisioned_gb', 'used_percent')
    list_filter = ('cluster', 'ds_type', 'environment')
    search_fields = ('name', 'cluster', 'ds_type')

@admin.register(StorageHistoricalLog)
class StorageHistoricalLogAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model StorageHistoricalLog di dashboard admin Django.
    """
    # Baris ini yang diperbaiki
    list_display = ('log_timestamp', 'storage_name', 'storage_alias', 'usage_tb', 'total_capacity_tb', 'iops', 'throughput_mbs') # <-- PERBAIKI DI SINI
    list_filter = ('storage_alias',)
    search_fields = ('storage_name', 'storage_alias')
    date_hierarchy = 'log_timestamp' # Mempermudah navigasi berdasarkan tanggal/waktu