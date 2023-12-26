# Generated by Django 4.2.6 on 2023-10-31 11:59

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
            name='RouteModel',
            fields=[
                ('route_id', models.AutoField(primary_key=True, serialize=False)),
                ('route_name', models.CharField(max_length=100)),
                ('route_start_point', models.CharField(max_length=100)),
                ('route_end_point', models.CharField(max_length=100)),
                ('route_areas', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified_on', models.DateTimeField(auto_now=True)),
                ('last_modified_by', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_by', models.CharField(blank=True, max_length=100, null=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='routes_route_model', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
