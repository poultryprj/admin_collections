# Generated by Django 4.2.6 on 2024-01-02 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor1', '0002_alter_vendor_table_alter_vendorcreditbalance_table_and_more'),
        ('shops1', '0003_alter_productrecieve_delete_reason'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productcategories',
            options={},
        ),
        migrations.AlterModelOptions(
            name='producttypes',
            options={},
        ),
        migrations.AlterField(
            model_name='productrecieve',
            name='vendorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vendor1.vendor'),
        ),
        migrations.AlterModelTable(
            name='associations',
            table='Associations',
        ),
        migrations.AlterModelTable(
            name='productcategories',
            table='ProductCategories',
        ),
        migrations.AlterModelTable(
            name='productissue',
            table='ProductIssue',
        ),
        migrations.AlterModelTable(
            name='productmaster',
            table='ProductMaster',
        ),
        migrations.AlterModelTable(
            name='productrecieve',
            table='ProductRecieve',
        ),
        migrations.AlterModelTable(
            name='producttypes',
            table='ProductTypes',
        ),
        migrations.AlterModelTable(
            name='shopbalance',
            table='ShopBalance',
        ),
        migrations.AlterModelTable(
            name='shopflexiblerate',
            table='ShopFlexibleRate',
        ),
        migrations.AlterModelTable(
            name='shopmodel',
            table='ShopModel',
        ),
        migrations.AlterModelTable(
            name='shopowner',
            table='ShopOwner',
        ),
        migrations.AlterModelTable(
            name='shopproductrates',
            table='ShopProductRates',
        ),
        migrations.AlterModelTable(
            name='shopproductrequest',
            table='ShopProductRequest',
        ),
        migrations.AlterModelTable(
            name='shoproute',
            table='ShopRoute',
        ),
    ]
