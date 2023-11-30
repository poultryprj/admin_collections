# Generated by Django 4.2.6 on 2023-11-29 05:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_associations_productcategories_productmaster_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategories',
            options={'verbose_name': 'Product Category', 'verbose_name_plural': 'Product Categories'},
        ),
        migrations.AlterModelOptions(
            name='producttypes',
            options={'verbose_name': 'Product Type', 'verbose_name_plural': 'Product Types'},
        ),
        migrations.AddField(
            model_name='productmaster',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_master_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_master_deleted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='last_modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_master_last_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='productmaster',
            name='last_modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='deleted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_deleted', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='last_modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shop_product_rates_last_modified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shopproductrates',
            name='last_modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
