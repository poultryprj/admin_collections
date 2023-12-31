# Generated by Django 4.2.6 on 2024-01-02 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetDistribution',
            fields=[
                ('asset_distribution_id', models.AutoField(primary_key=True, serialize=False)),
                ('distribution_date_and_time', models.DateTimeField()),
                ('assets_consumer_type', models.CharField(max_length=255)),
                ('distribution_to_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=30)),
                ('remarks', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'AssetDistribution',
            },
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('asset_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=255)),
                ('asset_types', models.CharField(max_length=255)),
                ('slowly_finished_product', models.CharField(blank=True, max_length=255)),
                ('long_lasting_products', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Assets_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Assets_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Assets_last_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Assets',
            },
        ),
        migrations.CreateModel(
            name='AssetStock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_stock_quantity', models.IntegerField()),
                ('asset_stock_weight', models.DecimalField(decimal_places=2, max_digits=30)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('asset_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.assets')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsStocks_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsStocks_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsStocks_last_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'AssetStock',
            },
        ),
        migrations.CreateModel(
            name='AssetPurchase',
            fields=[
                ('asset_purchase_id', models.AutoField(primary_key=True, serialize=False)),
                ('purchase_on', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=30)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('remarks', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('asset_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='asset.assets')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsPurchase_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsPurchase_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='AssetsPurchase_last_modified', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'AssetPurchase',
            },
        ),
    ]
