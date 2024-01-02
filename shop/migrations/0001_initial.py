# Generated by Django 4.2.6 on 2024-01-02 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('route', '0001_initial'),
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Associations',
            fields=[
                ('association_id', models.IntegerField(primary_key=True, serialize=False)),
                ('association_name', models.CharField(max_length=500)),
                ('association_sequence', models.IntegerField(default=None, null=True)),
            ],
            options={
                'db_table': 'Associations',
            },
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('product_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='ProductIssue',
            fields=[
                ('product_issue_id', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField(null=True)),
                ('paper_rate', models.FloatField()),
                ('boiler_size', models.CharField(max_length=20)),
                ('issue_birds', models.CharField(max_length=20)),
                ('birds_weight', models.FloatField()),
                ('daily_rate', models.FloatField()),
                ('issue_amount', models.FloatField()),
                ('entry_source', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('longtitude', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ProductIssue',
            },
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_value_on', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'ProductMaster',
            },
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('product_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ProductTypes',
            },
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
            ],
            options={
                'db_table': 'ShopModel',
            },
        ),
        migrations.CreateModel(
            name='ShopRoute',
            fields=[
                ('shop_route_id', models.AutoField(primary_key=True, serialize=False)),
                ('shop_order', models.CharField(max_length=10, null=True)),
                ('route_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='route.routemodel')),
                ('shop_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
            options={
                'db_table': 'ShopRoute',
            },
        ),
        migrations.CreateModel(
            name='ShopProductRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_request_date_time', models.DateTimeField(null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=20, null=True)),
                ('status', models.CharField(default='Rejected', max_length=100)),
                ('delivery_date_time', models.DateTimeField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopProductRequest_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopProductRequest_deleted', to=settings.AUTH_USER_MODEL)),
                ('driverId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopProductRequest_last_modified', to=settings.AUTH_USER_MODEL)),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productmaster')),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
            options={
                'db_table': 'ShopProductRequest',
            },
        ),
        migrations.CreateModel(
            name='ShopProductRates',
            fields=[
                ('shop_product_rates_id', models.AutoField(primary_key=True, serialize=False)),
                ('rate_margin', models.IntegerField()),
                ('flexible_yn', models.CharField(max_length=15, null=True)),
                ('flexible_formula', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('ProductId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productmaster')),
                ('associationId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.associations')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_last_modified', to=settings.AUTH_USER_MODEL)),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
            options={
                'db_table': 'ShopProductRates',
            },
        ),
        migrations.CreateModel(
            name='ShopOwner',
            fields=[
                ('owner_id', models.AutoField(primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=100, null=True)),
                ('owner_contactNo', models.CharField(max_length=15, null=True)),
                ('owner_alternateNo', models.CharField(max_length=15, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shops_shop_owners', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopOwner_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ShopOwner_last_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ShopOwner',
            },
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='shop_ownerId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopowner'),
        ),
        migrations.CreateModel(
            name='ShopFlexibleRate',
            fields=[
                ('shop_flexible_rate_id', models.AutoField(primary_key=True, serialize=False)),
                ('flexible_rate_date', models.DateField()),
                ('flexible_rate', models.FloatField()),
                ('flexible_formula', models.IntegerField(null=True)),
                ('sell_rate', models.FloatField()),
                ('with_skin', models.FloatField()),
                ('without_skin', models.FloatField()),
                ('sms_send_yn', models.CharField(default='No', max_length=15, null=True)),
                ('sms_replyId', models.IntegerField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_flexible_rate_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_flexible_rate_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_flexible_rate_last_modified', to=settings.AUTH_USER_MODEL)),
                ('product_typeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttypes')),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
            options={
                'db_table': 'ShopFlexibleRate',
            },
        ),
        migrations.CreateModel(
            name='ShopBalance',
            fields=[
                ('shop_balance_id', models.AutoField(primary_key=True, serialize=False)),
                ('balance_date', models.DateField()),
                ('balance', models.FloatField()),
                ('active', models.CharField(default='Yes', max_length=15, null=True)),
                ('adjustment_amount', models.FloatField(null=True)),
                ('adjustment_remark', models.TextField(null=True)),
                ('balance_utc_date', models.DateTimeField(auto_now_add=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_balance_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_balance_deleted', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_balance_last_modified', to=settings.AUTH_USER_MODEL)),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
            options={
                'db_table': 'ShopBalance',
            },
        ),
        migrations.CreateModel(
            name='ProductRecieve',
            fields=[
                ('product_record_id', models.AutoField(primary_key=True, serialize=False)),
                ('recieved_date', models.DateField(null=True)),
                ('paper_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('recieved_quantity', models.IntegerField()),
                ('recieved_weight', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tcs_rate', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('tcs_value', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('recieved_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('source_vehicle_id', models.IntegerField()),
                ('source_driver_id', models.IntegerField()),
                ('challan_no', models.CharField(max_length=150)),
                ('entry_source', models.IntegerField()),
                ('latitude', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('longtitude', models.DecimalField(decimal_places=5, max_digits=20, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('delete_reason', models.CharField(blank=True, max_length=150, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_received_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_received_deleted', to=settings.AUTH_USER_MODEL)),
                ('driverId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('last_modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_received_last_modified', to=settings.AUTH_USER_MODEL)),
                ('productId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productmaster')),
                ('product_typeId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttypes')),
                ('vehicleId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehicle')),
            ],
            options={
                'db_table': 'ProductRecieve',
            },
        ),
    ]
