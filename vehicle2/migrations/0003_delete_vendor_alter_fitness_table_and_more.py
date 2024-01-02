# Generated by Django 4.2.6 on 2024-01-02 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0004_alter_assetpurchase_vendor_id_and_more'),
        ('shops1', '0004_alter_productcategories_options_and_more'),
        ('vehicle2', '0002_vehiclerunning'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
        migrations.AlterModelTable(
            name='fitness',
            table='Fitness',
        ),
        migrations.AlterModelTable(
            name='insurancecompany',
            table='InsuranceCompany',
        ),
        migrations.AlterModelTable(
            name='vehicle',
            table='Vehicle',
        ),
        migrations.AlterModelTable(
            name='vehicleinsurance',
            table='VehicleInsurance',
        ),
        migrations.AlterModelTable(
            name='vehiclemakeby',
            table='VehicleMakeBy',
        ),
        migrations.AlterModelTable(
            name='vehiclemodel',
            table='VehicleModel',
        ),
        migrations.AlterModelTable(
            name='vehiclepermit',
            table='VehiclePermit',
        ),
        migrations.AlterModelTable(
            name='vehiclepollution',
            table='VehiclePollution',
        ),
        migrations.AlterModelTable(
            name='vehiclerunning',
            table='VehicleRunning',
        ),
        migrations.AlterModelTable(
            name='vehicletax',
            table='VehicleTax',
        ),
        migrations.AlterModelTable(
            name='vehicletype',
            table='VehicleType',
        ),
    ]
