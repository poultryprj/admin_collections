# Generated by Django 4.2.6 on 2023-11-28 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shoproute'),
    ]

    operations = [
        migrations.CreateModel(
            name='Associations',
            fields=[
                ('association_id', models.IntegerField(primary_key=True, serialize=False)),
                ('association_name', models.CharField(max_length=500)),
                ('association_equence', models.IntegerField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategories',
            fields=[
                ('product_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMaster',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_value_on', models.CharField(max_length=100)),
                ('product_categoryId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productcategories')),
            ],
        ),
        migrations.CreateModel(
            name='ProductTypes',
            fields=[
                ('product_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShopProductRates',
            fields=[
                ('shop_product_rates_id', models.AutoField(primary_key=True, serialize=False)),
                ('rate_margin', models.IntegerField()),
                ('flexible_yn', models.CharField(max_length=15, null=True)),
                ('flexible_formula', models.IntegerField(null=True)),
                ('ProductId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.productmaster')),
                ('associationId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.associations')),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.shopmodel')),
            ],
        ),
        migrations.AddField(
            model_name='productmaster',
            name='product_typeId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.producttypes'),
        ),
    ]
