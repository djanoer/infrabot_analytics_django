# infrabot_analytics_django/core/models.py
from django.db import models

class ConfigurationSetting(models.Model):
    """
    Model untuk menyimpan konfigurasi bot secara dinamis dari sheet 'Konfigurasi'.
    Menggantikan sebagian besar KUNCI_KONFIG di Konstanta.js yang bisa diubah oleh admin.
    """
    key = models.CharField(max_length=255, unique=True, help_text="Kunci konfigurasi (misalnya, THRESHOLD_VM_UPTIME_DAYS)")
    value = models.TextField(help_text="Nilai konfigurasi (bisa berupa string, JSON string, atau angka)")
    description = models.TextField(blank=True, null=True, help_text="Deskripsi singkat untuk konteks konfigurasi")
    last_updated = models.DateTimeField(auto_now=True) # auto_now=True akan update setiap save

    class Meta:
        verbose_name = "Pengaturan Konfigurasi"
        verbose_name_plural = "Pengaturan Konfigurasi"
        ordering = ['key']

    def __str__(self):
        return self.key

    def get_parsed_value(self):
        """
        Mencoba mem-parsing nilai sebagai JSON, array, atau angka jika memungkinkan.
        Mirip dengan logika parsing di bacaKonfigurasi()
        """
        import json
        from core.utils import parse_locale_number # Pastikan core.utils sudah ada

        try:
            # Coba parse sebagai JSON
            parsed = json.loads(self.value)
            return parsed
        except json.JSONDecodeError:
            pass

        # Coba parse sebagai angka
        # Memeriksa string jika bisa dikonversi ke float (untuk desimal) atau int
        if self.value.replace('.', '', 1).isdigit() or (self.value.startswith('-') and self.value[1:].replace('.', '', 1).isdigit()):
            return parse_locale_number(self.value)

        # Coba parse sebagai array (string dipisahkan koma)
        if ',' in self.value:
            return [item.strip() for item in self.value.split(',') if item.strip()]

        # Default ke string
        return self.value