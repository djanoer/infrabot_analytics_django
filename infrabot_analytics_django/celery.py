# infrabot_analytics_django/infrabot_analytics_django/celery.py

import os
from celery import Celery

# Mengatur 'DJANGO_SETTINGS_MODULE' agar Celery tahu di mana mencari pengaturan Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infrabot_analytics_django.settings')

# Membuat instance aplikasi Celery
app = Celery('infrabot_analytics_django')

# Menggunakan konfigurasi pengaturan Django untuk Celery
# Ini berarti semua pengaturan Celery akan didefinisikan di settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Memuat tugas dari semua aplikasi Django yang terdaftar
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')