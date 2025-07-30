# infrabot_analytics_django/tickets/models.py
from django.db import models

class Ticket(models.Model):
    """
    Model untuk data tiket utilisasi. Menggantikan sheet 'NAMA_SHEET_TIKET'.
    """
    ticket_id = models.CharField(max_length=100, unique=True, verbose_name="ID Tiket")
    vm_name = models.CharField(max_length=255, verbose_name="Nama VM Terkait")
    criticality = models.CharField(max_length=100, null=True, blank=True, verbose_name="Kritikalitas VM")
    link = models.URLField(max_length=500, verbose_name="Link Tiket")
    category = models.CharField(max_length=100, verbose_name="Kategori Tiket") # Provisioning, Utilisasi, dll.
    created_date = models.DateField(null=True, blank=True, verbose_name="Tanggal Buat")
    follow_up_date = models.DateField(null=True, blank=True, verbose_name="Tanggal Follow Up")
    status = models.CharField(max_length=100, verbose_name="Status Tiket") # Active, Done, Closed, dll.
    action_needed = models.TextField(null=True, blank=True, verbose_name="Action Needed")
    done_date = models.DateField(null=True, blank=True, verbose_name="Tanggal Selesai")
    dev_ops = models.CharField(max_length=255, null=True, blank=True, verbose_name="DEV/OPS Penanggung Jawab")
    description = models.TextField(null=True, blank=True, verbose_name="Keterangan")

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tiket Utilisasi"
        verbose_name_plural = "Tiket Utilisasi"
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['ticket_id']),
            models.Index(fields=['vm_name']),
            models.Index(fields=['status']),
            models.Index(fields=['follow_up_date']),
        ]

    def __str__(self):
        return f"{self.ticket_id} - {self.status}"