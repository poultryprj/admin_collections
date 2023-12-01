from django.contrib import admin
from .models import Vehicle, Vendor, ProductRecieve, VehicalMakeBy
# Register your models here.


class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')

    search_fields = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')

    list_display_links = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')
    
    


class VendorModelAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_type')

    search_fields = ('vendor_id', 'vendor_name', 'vendor_type')

    list_display_links = ('vendor_id', 'vendor_name', 'vendor_type')




class ProductRecieveModelAdmin(admin.ModelAdmin):
    list_display = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')

    search_fields = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId')

    list_display_links = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')



class VehicalMakeByModelAdmin(admin.ModelAdmin):
    list_display = ('vehical_make_id', 'vehical_make_by' )

    search_fields = ('vehical_make_id', 'vehical_make_by')

    list_display_links = ('vehical_make_id', 'vehical_make_by')


admin.site.register(VehicalMakeBy,VehicalMakeByModelAdmin)
admin.site.register(Vehicle,VehicleModelAdmin)
admin.site.register(Vendor,VendorModelAdmin)
admin.site.register(ProductRecieve,ProductRecieveModelAdmin)