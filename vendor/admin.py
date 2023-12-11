from django.contrib import admin
from .models import Vendor, VendorProduct
# Register your models here.



class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    
    search_fields = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_address', 'vendor_active')

    list_display_links = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')




class VendorProductAdmin(admin.ModelAdmin):
    list_display = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds')

    list_display_links = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds')







admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorProduct, VendorProductAdmin)