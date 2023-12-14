# Generated by Django 4.2.6 on 2023-12-14 11:56

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
            name='InsuranceCompany',
            fields=[
                ('insurance_company_id', models.AutoField(primary_key=True, serialize=False)),
                ('insurance_company_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('registration_no', models.CharField(max_length=50)),
                ('owner_name', models.CharField(max_length=100)),
                ('vehicle_details', models.CharField(max_length=200)),
                ('fuel_type', models.CharField(max_length=50)),
                ('no_of_wheel', models.IntegerField()),
                ('carrier_type', models.CharField(max_length=100)),
                ('registration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='VehicleMakeBy',
            fields=[
                ('vehicle_make_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_make_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('vehicle_model_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_model', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('vehicle_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor_name', models.CharField(max_length=150)),
                ('vendor_type', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleTax',
            fields=[
                ('tax_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_tax_from_Date', models.DateField()),
                ('vehicle_tax_to_Date', models.DateField()),
                ('vehicle_tax_type', models.CharField(max_length=255)),
                ('vehicle_environment_tax', models.DecimalField(decimal_places=2, max_digits=30)),
                ('vehicle_professional_tax', models.DecimalField(decimal_places=2, max_digits=30)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_tax_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_tax_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_tax_modify_by', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePollution',
            fields=[
                ('pollution_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_pollution_from_Date', models.DateField()),
                ('vehicle_pollution_to_Date', models.DateField()),
                ('vehicle_pollution_value', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_pollution_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_pollution_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_pollution_modify_by', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePermit',
            fields=[
                ('permit_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_permit_from_Date', models.DateField()),
                ('vehicle_permit_to_Date', models.DateField()),
                ('vehicle_permit_type', models.CharField(max_length=255)),
                ('vehicle_permit_id', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('lastModifiedOn', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_permit_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_permit_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_permit_modify_by', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleInsurance',
            fields=[
                ('insurance_id', models.AutoField(primary_key=True, serialize=False)),
                ('insurance_from_date', models.DateField()),
                ('insurance_to_date', models.DateField()),
                ('insurance_amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('insurance_paid_amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_insurance_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_insurance_details_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('insurance_company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.insurancecompany')),
                ('last_modified_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_insurance_modify_by', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicle')),
            ],
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_make_Id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehiclemakeby'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehiclemodel'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicletype'),
        ),
        migrations.CreateModel(
            name='Fitness',
            fields=[
                ('fitness_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_fitness_from_date', models.DateField()),
                ('vehicle_fitness_to_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('created_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_fitness_created_by', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fitness_details_deleted_by', to=settings.AUTH_USER_MODEL)),
                ('last_modified_by_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vehicle_fitness_modify_by', to=settings.AUTH_USER_MODEL)),
                ('vehicle_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle2.vehicle')),
            ],
        ),
    ]