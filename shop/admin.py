from django.contrib import admin
from .models import ShopModel, ShopOwner, ShopRoute

# Register your models here.


class ShopModelAdmin(admin.ModelAdmin):

    list_display = ('shop_id', 'shop_code', 'shop_name', 'shop_area', 'shop_latitude', 'shop_longitude', 'shop_address', 'shop_pincode', 'shop_distance', 'shop_mobileNo', 'shop_alternateNo', 'shop_ownerId', 'shop_type', 'shop_status')

    search_fields = ('shop_code', 'shop_name', 'shop_area', 'shop_pincode')

    list_display_links = ('shop_id','shop_code', 'shop_name', 'shop_area')



class ShopOwnerModelAdmin(admin.ModelAdmin):
    list_display = ('owner_id', 'owner_name', 'owner_contactNo', 'owner_alternateNo', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('owner_id','owner_name', 'created_on')

    list_display_links = ('owner_id','owner_name', 'owner_contactNo', 'owner_alternateNo')



class ShopRouteAdmin(admin.ModelAdmin):
    list_display = ('shop_route_id', 'route_id', 'shop_id', 'shop_order')

    search_fields = ('shop_route_id','route_id', 'shop_id', 'shop_order')

    list_display_links = ('shop_route_id','route_id', 'shop_id', 'shop_order')




admin.site.register(ShopOwner, ShopOwnerModelAdmin)
admin.site.register(ShopModel,ShopModelAdmin)
admin.site.register(ShopRoute,ShopRouteAdmin)