from django.contrib import admin
from .models import Vendor
# Register your models here.



class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    
    search_fields = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_address', 'vendor_active')

    list_display_links = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')


admin.site.register(Vendor, VendorAdmin)