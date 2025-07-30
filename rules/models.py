# infrabot_analytics_django/rules/models.py
from django.db import models

class MigrationRule(models.Model):
    """
    Model untuk logika migrasi datastore. Menggantikan sheet 'Logika Migrasi'.
    """
    recognized_type = models.CharField(max_length=100, unique=True, verbose_name="Tipe Teridentifikasi (mis: VSPA)")
    alias = models.CharField(max_length=100, null=True, blank=True, help_text="Alias Tipe (opsional)")
    priority_destinations = models.JSONField(default=list, help_text="Daftar tipe tujuan prioritas (JSON Array)")

    class Meta:
        verbose_name = "Aturan Migrasi"
        verbose_name_plural = "Aturan Migrasi"

    def __str__(self):
        return self.recognized_type

class ProvisioningRule(models.Model):
    """
    Model untuk aturan provisioning VM. Menggantikan sheet 'Rule Provisioning'.
    """
    criticality = models.CharField(max_length=100, unique=True, verbose_name="Kritikalitas (mis: CRITICAL, DEFAULT)")
    io_profile = models.CharField(max_length=50, default="*", verbose_name="Profil I/O (mis: High, Normal, *)")
    vcenter_target = models.CharField(max_length=100, verbose_name="vCenter Target")
    priority1_clusters = models.JSONField(default=list, help_text="Klaster Prioritas 1 (JSON Array)")
    priority2_clusters = models.JSONField(default=list, help_text="Klaster Prioritas 2 (JSON Array)")
    priority3_clusters = models.JSONField(default=list, help_text="Klaster Prioritas 3 (JSON Array)")
    excluded_clusters = models.JSONField(default=list, blank=True, help_text="Klaster yang Dikecualikan (JSON Array)")
    storage_priority1 = models.JSONField(default=list, help_text="Tipe Storage Prioritas 1 (JSON Array)")
    storage_priority2 = models.JSONField(default=list, help_text="Tipe Storage Prioritas 2 (JSON Array)")

    class Meta:
        verbose_name = "Aturan Provisioning"
        verbose_name_plural = "Aturan Provisioning"

    def __str__(self):
        return f"Kritikalitas: {self.criticality} - I/O: {self.io_profile}"

class ClusterPolicy(models.Model):
    """
    Model untuk kebijakan overcommit cluster. Menggantikan sheet 'Kebijakan Overcommit Cluster'.
    """
    cluster_name = models.CharField(max_length=100, unique=True, verbose_name="Nama Cluster")
    physical_cpu_cores = models.IntegerField(verbose_name="Physical CPU Cores")
    cpu_overcommit_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="CPU Overcommit Ratio")
    physical_memory_tb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Physical Memory (TB)")
    memory_overcommit_ratio = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Memory Overcommit Ratio")

    class Meta:
        verbose_name = "Kebijakan Overcommit Cluster"
        verbose_name_plural = "Kebijakan Overcommit Cluster"

    def __str__(self):
        return self.cluster_name