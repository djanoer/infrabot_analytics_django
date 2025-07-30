# infrabot_analytics_django/core/admin.py
from django.contrib import admin
from .models import ConfigurationSetting

@admin.register(ConfigurationSetting)
class ConfigurationSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'last_updated')
    search_fields = ('key',)
    list_filter = ('last_updated',)
    # Anda bisa menambahkan form kustom untuk parsing nilai di admin nanti