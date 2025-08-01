# Generated by Django 5.2.4 on 2025-07-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datastore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Nama Datastore')),
                ('cluster', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cluster')),
                ('environment', models.CharField(blank=True, max_length=100, null=True, verbose_name='Environment')),
                ('ds_type', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tipe Datastore')),
                ('capacity_gb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Capacity (GB)')),
                ('provisioned_gb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Provisioned (GB)')),
                ('used_percent', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Used (%)')),
                ('capacity_tb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Capacity (TB)')),
                ('provisioned_tb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Provisioned (TB)')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Datastore',
                'verbose_name_plural': 'Datastores',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='datastores__name_59a1af_idx'), models.Index(fields=['cluster'], name='datastores__cluster_c2550d_idx'), models.Index(fields=['ds_type'], name='datastores__ds_type_49e4bf_idx')],
            },
        ),
        migrations.CreateModel(
            name='StorageHistoricalLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_timestamp', models.DateTimeField(verbose_name='Timestamp Log')),
                ('storage_name', models.CharField(max_length=255, verbose_name='Storage Name (from Report)')),
                ('storage_alias', models.CharField(max_length=255, verbose_name='Storage Alias (from Config Map)')),
                ('usage_tb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Usage (TB)')),
                ('total_capacity_tb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Total Capacity (TB)')),
                ('snapshot_tb', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Snapshot (TB)')),
                ('latency_ms', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Latency (ms)')),
                ('iops', models.IntegerField(default=0, verbose_name='IOPS')),
                ('throughput_mbs', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Throughput (MB/s)')),
                ('controller_cpu_percent', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Controller CPU (%)')),
                ('data_reduction_ratio', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Data Reduction Ratio')),
                ('datastore_count', models.IntegerField(default=0, verbose_name='Datastore Count')),
            ],
            options={
                'verbose_name': 'Log Historis Storage',
                'verbose_name_plural': 'Log Historis Storage',
                'ordering': ['-log_timestamp'],
                'indexes': [models.Index(fields=['log_timestamp'], name='datastores__log_tim_1a033c_idx'), models.Index(fields=['storage_alias'], name='datastores__storage_9447d6_idx')],
            },
        ),
    ]
