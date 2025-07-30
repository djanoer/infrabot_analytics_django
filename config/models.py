# infrabot_analytics_django/config/models.py
from django.db import models

class StorageAliasMap(models.Model):
    """
    Model untuk MAP_ALIAS_STORAGE. Menggantikan JSON di sheet Konfigurasi.
    Ini memungkinkan pemetaan satu kunci utama ke beberapa alias storage.
    """
    main_key = models.CharField(max_length=100, unique=True, verbose_name="Kunci Utama Storage (mis: VSPA)")
    aliases = models.JSONField(default=list, help_text="Daftar alias untuk storage ini (JSON Array, mis: [\"VSP\", \"HPE VSP A\"])")

    class Meta:
        verbose_name = "Pemetaan Alias Storage"
        verbose_name_plural = "Pemetaan Alias Storage"

    def __str__(self):
        return self.main_key

class StorageCapacityMap(models.Model):
    """
    Model untuk MAP_KAPASITAS_STORAGE.
    """
    storage_alias = models.CharField(max_length=100, unique=True, verbose_name="Alias Storage")
    total_capacity_tb = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Kapasitas (TB)")

    class Meta:
        verbose_name = "Kapasitas Storage"
        verbose_name_plural = "Kapasitas Storage"

    def __str__(self):
        return self.storage_alias

class CriticalityScore(models.Model):
    """
    Model untuk SKOR_KRITIKALITAS.
    """
    level = models.CharField(max_length=100, unique=True, verbose_name="Level Kritikalitas (mis: CRITICAL, HIGH)")
    score_value = models.IntegerField(verbose_name="Nilai Skor")

    class Meta:
        verbose_name = "Skor Kritikalitas"
        verbose_name_plural = "Skor Kritikalitas"

    def __str__(self):
        return self.level

class EnvironmentMapping(models.Model):
    """
    Model untuk PEMETAAN_ENVIRONMENT.
    """
    keyword = models.CharField(max_length=100, unique=True, verbose_name="Kata Kunci di Nama Datastore")
    environment_name = models.CharField(max_length=100, verbose_name="Nama Environment")

    class Meta:
        verbose_name = "Pemetaan Environment"
        verbose_name_plural = "Pemetaan Environment"

    def __str__(self):
        return f"{self.keyword} -> {self.environment_name}"

class SystemLimit(models.Model):
    """
    Model untuk SYSTEM_LIMITS.
    """
    key = models.CharField(max_length=255, unique=True, verbose_name="Kunci Batasan Sistem (mis: LOG_CHANGE_ARCHIVE_THRESHOLD)")
    value = models.TextField(help_text="Nilai batasan (bisa angka, JSON string, dll.)")

    class Meta:
        verbose_name = "Batasan Sistem"
        verbose_name_plural = "Batasan Sistem"

    def __str__(self):
        return self.key

    def get_parsed_value(self):
        """Mencoba mem-parsing nilai sebagai JSON atau angka."""
        import json
        try:
            return json.loads(self.value)
        except json.JSONDecodeError:
            if self.value.isdigit():
                return int(self.value)
            return self.value

class ThresholdSetting(models.Model):
    """
    Model untuk THRESHOLD_DS_USED_PERCENT, THRESHOLD_VM_UPTIME_DAYS, dll.
    """
    key = models.CharField(max_length=255, unique=True, verbose_name="Kunci Threshold (mis: THRESHOLD_DS_USED_PERCENT)")
    value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Nilai Threshold")

    class Meta:
        verbose_name = "Pengaturan Threshold"
        verbose_name_plural = "Pengaturan Threshold"

    def __str__(self):
        return self.key

class DataExclusionKeyword(models.Model):
    """
    Model untuk KATA_KUNCI_DS_DIKECUALIKAN.
    """
    keyword = models.CharField(max_length=100, unique=True, verbose_name="Kata Kunci Pengecualian Datastore")

    class Meta:
        verbose_name = "Kata Kunci Pengecualian Data"
        verbose_name_plural = "Kata Kunci Pengecualian Data"

    def __str__(self):
        return self.keyword