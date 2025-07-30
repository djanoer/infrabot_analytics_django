# infrabot_analytics_django/vms/models.py
from django.db import models

# Import CustomUser di dalam Model VMNote
# Ini dilakukan untuk menghindari circular dependency saat aplikasi dimuat,
# karena CustomUser ada di aplikasi 'users' yang mungkin dimuat setelah 'vms'.
# Cara terbaik adalah mengimpornya di dalam method atau di dalam Model itu sendiri
# jika itu adalah ForeignKey/OneToOneField.
from users.models import CustomUser # <-- Pastikan baris ini ada


class VM(models.Model):
    """
    Model untuk data Virtual Machine. Menggantikan sheet 'Data VM Utama'.
    """
    # Identifiers
    primary_key = models.CharField(max_length=255, unique=True, verbose_name="Primary Key")
    name = models.CharField(max_length=255, verbose_name="Virtual Machine")
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP Address")

    # State & Health
    state = models.CharField(max_length=50, default="poweredOff", verbose_name="State") # poweredOn, poweredOff
    uptime_days = models.IntegerField(null=True, blank=True, verbose_name="Uptime (Hari)")
    health_score = models.IntegerField(default=100, verbose_name="Skor Kesehatan (0-100)") # Hasil kalkulasi Analisis.js

    # Resource Allocation
    cpu = models.IntegerField(default=0, verbose_name="CPU (vCPU)")
    memory_gb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Memory (GB)")
    provisioned_gb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Provisioned (GB)")
    provisioned_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Provisioned (TB)") # Diambil dari sheet atau dikonversi

    # Location & Categorization
    vcenter = models.CharField(max_length=100, verbose_name="vCenter")
    cluster = models.CharField(max_length=100, verbose_name="Cluster")
    datastore_name = models.CharField(max_length=255, verbose_name="Datastore") # Nama datastore, bisa pakai Foreign Key ke model Datastore nanti
    criticality = models.CharField(max_length=100, verbose_name="Kritikalitas BIA")
    environment = models.CharField(max_length=100, verbose_name="Environment")
    app_group = models.CharField(max_length=255, null=True, blank=True, verbose_name="Aplikasi BIA")
    dev_ops = models.CharField(max_length=255, null=True, blank=True, verbose_name="DEV/OPS")
    guest_os = models.CharField(max_length=255, null=True, blank=True, verbose_name="Guest OS")
    host = models.CharField(max_length=255, null=True, blank=True, verbose_name="Host")

    # Management & Tickets
    provisioning_ticket_no = models.CharField(max_length=100, null=True, blank=True, verbose_name="No Tiket Provisioning")
    setup_date = models.DateField(null=True, blank=True, verbose_name="Tanggal Setup")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Virtual Machine"
        verbose_name_plural = "Virtual Machines"
        ordering = ['name'] # Default ordering
        # Menambahkan indeks untuk field yang sering dicari
        indexes = [
            models.Index(fields=['primary_key']),
            models.Index(fields=['name']),
            models.Index(fields=['ip_address']),
            models.Index(fields=['cluster']),
            models.Index(fields=['datastore_name']),
        ]


    def __str__(self):
        return f"{self.name} ({self.primary_key})"

class VMHistoryLog(models.Model):
    """
    Model untuk mencatat riwayat perubahan VM. Menggantikan sheet 'Log Perubahan'.
    """
    vm = models.ForeignKey(VM, on_delete=models.SET_NULL, related_name='history_logs',
                           null=True, blank=True,
                           help_text="Relasi ke VM yang berubah (jika masih ada)")
    vm_primary_key = models.CharField(max_length=255, verbose_name="VM Primary Key")
    vm_name_at_log = models.CharField(max_length=255, verbose_name="Nama VM Saat Log")
    log_timestamp = models.DateTimeField(verbose_name="Timestamp Log")
    action = models.CharField(max_length=50, verbose_name="Aksi (PENAMBAHAN, MODIFIKASI, PENGHAPUSAN)")
    sheet_source = models.CharField(max_length=100, verbose_name="Sumber Sheet")
    old_value = models.TextField(blank=True, null=True, verbose_name="Nilai Lama")
    new_value = models.TextField(blank=True, null=True, verbose_name="Nilai Baru")
    detail = models.TextField(blank=True, null=True, verbose_name="Detail Perubahan")
    entity_type = models.CharField(max_length=50, verbose_name="Tipe Entitas (VM/Datastore)") # Untuk membedakan log VM dan Datastore

    class Meta:
        verbose_name = "Log Riwayat VM/Datastore"
        verbose_name_plural = "Log Riwayat VM/Datastore"
        ordering = ['-log_timestamp'] # Urutkan dari terbaru
        indexes = [
            models.Index(fields=['vm_primary_key']),
            models.Index(fields=['log_timestamp']),
            models.Index(fields=['action']),
        ]

    def __str__(self):
        return f"{self.action} - {self.vm_name_at_log} ({self.log_timestamp.strftime('%Y-%m-%d %H:%M')})"

class VMNote(models.Model):
    """
    Model untuk catatan spesifik per VM. Menggantikan sheet 'Catatan VM'.
    """
    # OneToOneField memastikan setiap VM hanya punya satu catatan dan sebaliknya.
    # on_delete=models.CASCADE berarti jika VM dihapus, catatannya juga ikut dihapus.
    vm = models.OneToOneField(VM, on_delete=models.CASCADE, related_name='note', verbose_name="Virtual Machine")
    note_text = models.TextField(verbose_name="Isi Catatan")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Timestamp Update")
    
    # Relasi ForeignKey ke CustomUser
    # Perhatikan import CustomUser yang sekarang ada di bagian atas file
    updated_by_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name="User Update")
    # Tetap pertahankan field ini untuk fallback jika updated_by_user null
    updated_by_telegram_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nama Telegram User (Fallback)")


    class Meta:
        verbose_name = "Catatan VM"
        verbose_name_plural = "Catatan VM"
        ordering = ['vm__name'] # Urutan berdasarkan nama VM


    def __str__(self):
        return f"Catatan untuk {self.vm.name}"