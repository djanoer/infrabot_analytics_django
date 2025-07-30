# infrabot_analytics_django/vms/admin.py
from django.contrib import admin
from .models import VM, VMHistoryLog, VMNote # Import Model yang sudah dibuat

@admin.register(VM) # Decorator ini mendaftarkan Model VM ke admin
class VMAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model VM di dashboard admin Django.
    """
    # field yang akan ditampilkan di daftar tabel (list view)
    list_display = ('name', 'primary_key', 'ip_address', 'state', 'vcenter', 'cluster', 'criticality', 'health_score')
    # field yang bisa digunakan untuk filter di sidebar
    list_filter = ('state', 'vcenter', 'cluster', 'criticality', 'environment')
    # field yang bisa digunakan untuk pencarian cepat
    search_fields = ('name', 'primary_key', 'ip_address', 'cluster', 'datastore_name')
    # raw_id_fields = ('note',) # Ini akan diaktifkan nanti setelah relasi final.

@admin.register(VMHistoryLog)
class VMHistoryLogAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model VMHistoryLog di dashboard admin Django.
    """
    list_display = ('log_timestamp', 'action', 'vm_primary_key', 'vm_name_at_log', 'entity_type', 'sheet_source')
    list_filter = ('action', 'entity_type', 'sheet_source')
    search_fields = ('vm_primary_key', 'vm_name_at_log', 'detail', 'old_value', 'new_value')
    date_hierarchy = 'log_timestamp' # Mempermudah navigasi berdasarkan tanggal/waktu

@admin.register(VMNote)
class VMNoteAdmin(admin.ModelAdmin):
    """
    Konfigurasi tampilan Model VMNote di dashboard admin Django.
    """
    list_display = ('vm', 'note_text', 'updated_by_user', 'updated_at') # Menggunakan 'updated_by_user'
    search_fields = ('vm__name', 'vm__primary_key', 'note_text') # Cari berdasarkan field di VM juga
    raw_id_fields = ('vm', 'updated_by_user') # <-- AKTIFKAN INI: Mempermudah pemilihan VM dan User