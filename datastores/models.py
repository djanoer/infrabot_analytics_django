# infrabot_analytics_django/datastores/models.py
from django.db import models

class Datastore(models.Model):
    """
    Model untuk data Datastore. Menggantikan sheet 'NAMA_SHEET_DATASTORE'.
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Nama Datastore")
    cluster = models.CharField(max_length=100, null=True, blank=True, verbose_name="Cluster")
    environment = models.CharField(max_length=100, null=True, blank=True, verbose_name="Environment")
    ds_type = models.CharField(max_length=100, null=True, blank=True, verbose_name="Tipe Datastore") # Analog dengan "Storage Alias"

    capacity_gb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Capacity (GB)")
    provisioned_gb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Provisioned (GB)")
    used_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Used (%)") # Percent of used capacity

    capacity_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Capacity (TB)")
    provisioned_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Provisioned (TB)")


    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Datastore"
        verbose_name_plural = "Datastores"
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['cluster']),
            models.Index(fields=['ds_type']),
        ]

    def __str__(self):
        return self.name

    @property
    def free_gb(self):
        """Menghitung ruang kosong dalam GB."""
        return self.capacity_gb - self.provisioned_gb

    @property
    def free_tb(self):
        """Menghitung ruang kosong dalam TB."""
        return self.capacity_tb - self.provisioned_tb

class StorageHistoricalLog(models.Model):
    """
    Model untuk log historis utilisisasi storage. Menggantikan sheet 'Log Storage Historis'.
    """
    log_timestamp = models.DateTimeField(verbose_name="Timestamp Log")
    storage_name = models.CharField(max_length=255, verbose_name="Storage Name (from Report)")
    storage_alias = models.CharField(max_length=255, verbose_name="Storage Alias (from Config Map)")
    usage_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Usage (TB)")
    total_capacity_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Total Capacity (TB)")
    snapshot_tb = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Snapshot (TB)")
    latency_ms = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Latency (ms)")
    iops = models.IntegerField(default=0, verbose_name="IOPS")
    throughput_mbs = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Throughput (MB/s)")
    controller_cpu_percent = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Controller CPU (%)")
    data_reduction_ratio = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Data Reduction Ratio")
    datastore_count = models.IntegerField(default=0, verbose_name="Datastore Count")

    class Meta:
        verbose_name = "Log Historis Storage"
        verbose_name_plural = "Log Historis Storage"
        ordering = ['-log_timestamp']
        indexes = [
            models.Index(fields=['log_timestamp']),
            models.Index(fields=['storage_alias']),
        ]

    def __str__(self):
        return f"Log {self.storage_name} at {self.log_timestamp.strftime('%Y-%m-%d %H:%M')}"