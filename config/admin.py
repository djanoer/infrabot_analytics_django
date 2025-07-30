# infrabot_analytics_django/config/admin.py
from django.contrib import admin
from .models import (
    StorageAliasMap, StorageCapacityMap, CriticalityScore,
    EnvironmentMapping, SystemLimit, ThresholdSetting, DataExclusionKeyword
)

@admin.register(StorageAliasMap)
class StorageAliasMapAdmin(admin.ModelAdmin):
    list_display = ('main_key', 'aliases_display')
    search_fields = ('main_key',)
    def aliases_display(self, obj):
        return ", ".join(obj.aliases) # Untuk menampilkan daftar alias sebagai string
    aliases_display.short_description = "Aliases"

@admin.register(StorageCapacityMap)
class StorageCapacityMapAdmin(admin.ModelAdmin):
    list_display = ('storage_alias', 'total_capacity_tb')
    search_fields = ('storage_alias',)

@admin.register(CriticalityScore)
class CriticalityScoreAdmin(admin.ModelAdmin):
    list_display = ('level', 'score_value')
    search_fields = ('level',)

@admin.register(EnvironmentMapping)
class EnvironmentMappingAdmin(admin.ModelAdmin):
    list_display = ('keyword', 'environment_name')
    search_fields = ('keyword', 'environment_name')

@admin.register(SystemLimit)
class SystemLimitAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

@admin.register(ThresholdSetting)
class ThresholdSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')
    search_fields = ('key',)

@admin.register(DataExclusionKeyword)
class DataExclusionKeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword',)
    search_fields = ('keyword',)