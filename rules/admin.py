# infrabot_analytics_django/rules/admin.py
from django.contrib import admin
from .models import MigrationRule, ProvisioningRule, ClusterPolicy

@admin.register(MigrationRule)
class MigrationRuleAdmin(admin.ModelAdmin):
    list_display = ('recognized_type', 'alias', 'priority_destinations_display')
    search_fields = ('recognized_type', 'alias')
    def priority_destinations_display(self, obj):
        return ", ".join(obj.priority_destinations) # Untuk menampilkan daftar tujuan sebagai string
    priority_destinations_display.short_description = "Tujuan Prioritas"

@admin.register(ProvisioningRule)
class ProvisioningRuleAdmin(admin.ModelAdmin):
    list_display = ('criticality', 'io_profile', 'vcenter_target')
    list_filter = ('criticality', 'io_profile', 'vcenter_target')
    search_fields = ('criticality', 'io_profile', 'vcenter_target')

@admin.register(ClusterPolicy)
class ClusterPolicyAdmin(admin.ModelAdmin):
    list_display = ('cluster_name', 'physical_cpu_cores', 'cpu_overcommit_ratio', 'physical_memory_tb', 'memory_overcommit_ratio')
    search_fields = ('cluster_name',)