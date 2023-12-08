from django.contrib import admin
from .models import Vehicle, Vendor, ProductRecieve, VehicleMakeBy, VehicleModel, VehicleType, Fitness
# Register your models here.


class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')

    search_fields = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')

    list_display_links = ('vehicle_id', 'registration_no', 'owner_name', 'vehicle_make_Id', 'vehicle_model','vehicle_type', 'vehicle_details', 'fuel_type', 'no_of_wheel', 'carrier_type', 'registration_date')
    
    


class VendorModelAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_type')

    search_fields = ('vendor_id', 'vendor_name', 'vendor_type')

    list_display_links = ('vendor_id', 'vendor_name', 'vendor_type')




class VehicleMakeByModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle_make_id', 'vehicle_make_by' )

    search_fields = ('vehicle_make_id', 'vehicle_make_by')

    list_display_links = ('vehicle_make_id', 'vehicle_make_by')



class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle_model_id', 'vehicle_model' )

    search_fields = ('vehicle_model_id', 'vehicle_model' )

    list_display_links = ('vehicle_model_id', 'vehicle_model' )




class VehicleTypeModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle_type_id', 'vehicle_type' )

    search_fields = ('vehicle_type_id', 'vehicle_type' )

    list_display_links = ('vehicle_type_id', 'vehicle_type' )



class ProductRecieveModelAdmin(admin.ModelAdmin):
    list_display = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')

    search_fields = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId')

    list_display_links = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')



class FitnessAdmin(admin.ModelAdmin):
    list_display = ('fitness_id', 'vehicle_id', 'vehicle_fitness_from_date', 'vehicle_fitness_to_date', 'created_by_id', 'last_modified_by_id', 'created_on', 'last_modified_on')

    search_fields = ('fitness_id', 'vehicle_id')

    list_display_links = ('fitness_id', 'vehicle_id')





admin.site.register(Vehicle,VehicleAdmin)
admin.site.register(Vendor,VendorModelAdmin)
admin.site.register(VehicleMakeBy,VehicleMakeByModelAdmin)
admin.site.register(VehicleModel,VehicleModelAdmin)
admin.site.register(VehicleType,VehicleTypeModelAdmin)
admin.site.register(ProductRecieve,ProductRecieveModelAdmin)
admin.site.register(Fitness,FitnessAdmin)