from django.contrib import admin
from .models import RouteModel

# Register your models here.

class RouteModelAdmin(admin.ModelAdmin):
    list_display = ('route_id', 'route_name', 'route_start_point', 'route_end_point', 'route_areas',  'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('route_name', 'route_start_point', 'route_end_point', 'route_areas')
    
    list_display_links= ('route_id', 'route_name', 'route_start_point', 'route_end_point', 'route_areas')

admin.site.register(RouteModel,RouteModelAdmin)
