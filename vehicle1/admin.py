from django.contrib import admin
from .models import InsuranceCompany, Vehicle, VehicleInsurance, VehiclePermit, Vendor, ProductRecieve, VehicleMakeBy, VehicleModel, VehicleType, Fitness
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


class FitnessAdmin(admin.ModelAdmin):
    list_display = ('fitness_id', 'vehicle_id', 'vehicle_fitness_from_date', 'vehicle_fitness_to_date', 'created_by_id', 'last_modified_by_id', 'created_on', 'last_modified_on')

    search_fields = ('fitness_id', 'vehicle_id')

    list_display_links = ('fitness_id', 'vehicle_id')



class VehicleInsuranceAdmin(admin.ModelAdmin):
    list_display = (
        'insurance_id', 'vehicle_id', 'insurance_company', 'insurance_from_date',
        'insurance_to_date', 'insurance_amount', 'insurance_paid_amount', 'created_by_id',
        'last_modified_by_id', 'created_on', 'last_modified_on', 'is_deleted', 'deleted_by',
    )

    search_fields = (
        'insurance_id', 'vehicle_id', 'insurance_company',
        'insurance_from_date', 'insurance_to_date', 'insurance_amount', 'insurance_paid_amount',
    )

    list_display_links = ('insurance_id', 'vehicle_id', 'insurance_company', 'insurance_from_date',
                          'insurance_to_date', 'insurance_amount', 'insurance_paid_amount',
                          'created_by_id', 'last_modified_by_id', 'created_on', 'last_modified_on',
                          'is_deleted', 'deleted_by',)

class InsuranceCompanyAdmin(admin.ModelAdmin):
    list_display = ('insurance_company_id', 'insurance_company_name')
    search_fields = ('insurance_company_id', 'insurance_company_name')
    list_display_links = ('insurance_company_id', 'insurance_company_name')


class VehiclePermitAdmin(admin.ModelAdmin):
    list_display = (
        'permit_id', 'vehicle_id', 'vehicle_permit_from_Date', 'vehicle_permit_to_Date',
        'vehicle_permit_type', 'vehicle_permit_id','created_by_id',
        'last_modified_by_id', 'created_on', 'lastModifiedOn', 'is_deleted', 'deleted_by',
    )

    search_fields = (
        'permit_id', 'vehicle_id', 'vehicle_permit_from_Date', 'vehicle_permit_to_Date',
        'vehicle_permit_type', 'vehicle_permit_id',
    )

    list_display_links = (
        'permit_id', 'vehicle_id', 'vehicle_permit_from_Date', 'vehicle_permit_to_Date',
        'vehicle_permit_type', 'vehicle_permit_id','created_by_id',
        'last_modified_by_id', 'created_on', 'lastModifiedOn', 'is_deleted', 'deleted_by',
                          )

admin.site.register(VehicleMakeBy,VehicleMakeByModelAdmin)
admin.site.register(VehicleModel,VehicleModelAdmin)
admin.site.register(VehicleType,VehicleTypeModelAdmin)
admin.site.register(Vehicle,VehicleModelAdmin)
admin.site.register(Vendor,VendorModelAdmin)
admin.site.register(ProductRecieve,ProductRecieveModelAdmin)
admin.site.register(Fitness,FitnessAdmin)
admin.site.register(VehicleInsurance,VehicleInsuranceAdmin)
admin.site.register(InsuranceCompany,InsuranceCompanyAdmin)
admin.site.register(VehiclePermit,VehiclePermitAdmin)
