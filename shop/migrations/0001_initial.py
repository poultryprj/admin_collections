# Generated by Django 4.2.6 on 2023-11-01 06:26

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
            name='ShopOwner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=100, null=True)),
                ('owner_contactNo', models.CharField(max_length=15, null=True)),
                ('owner_alternateNo', models.CharField(max_length=15, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_by', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shops_shop_owners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopModel',
            fields=[
                ('shop_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_code', models.CharField(max_length=10, null=True)),
                ('shop_name', models.CharField(max_length=100, null=True)),
                ('shop_area', models.CharField(max_length=100, null=True)),
                ('shop_latitude', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('shop_longitude', models.DecimalField(decimal_places=5, max_digits=10, null=True)),
                ('shop_address', models.CharField(max_length=100, null=True)),
                ('shop_pincode', models.IntegerField(null=True)),
                ('shop_distance', models.CharField(max_length=10, null=True)),
                ('shop_mobileNo', models.CharField(max_length=15, null=True)),
                ('shop_alternateNo', models.CharField(max_length=15, null=True)),
                ('shop_type', models.CharField(max_length=20, null=True)),
                ('shop_status', models.CharField(max_length=15, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('shop_ownerId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopowner')),
            ],
        ),
    ]
