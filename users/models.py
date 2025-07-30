# infrabot_analytics_django/users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Model user kustom yang memperluas user default Django.
    Menggantikan sheet 'Hak Akses'.
    """
    telegram_user_id = models.CharField(max_length=50, unique=True, null=True, blank=True,
                                        help_text="ID unik pengguna Telegram")
    telegram_username = models.CharField(max_length=100, null=True, blank=True)
    # Kolom 'email' dan 'is_staff' (untuk admin) sudah ada di AbstractUser

    class Meta:
        verbose_name = "Pengguna Bot"
        verbose_name_plural = "Pengguna Bot"

    def __str__(self):
        return self.username or self.email or str(self.telegram_user_id)

    def get_user_access_map_entry(self):
        """
        Mengembalikan format data yang mirip dengan userAccessMap di Apps Script.
        Digunakan untuk otorisasi dan identifikasi user Telegram.
        """
        return {
            'email': self.email,
            'role': 'Admin' if self.is_staff else 'User', # Mengasumsikan is_staff sebagai admin
            'first_name': self.first_name, # Untuk user-friendly display
            'user_id': self.telegram_user_id # Untuk pengenalan Telegram
        }