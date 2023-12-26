from django.contrib import admin
from .models import Vendor, VendorProduct, VendorOpeningBalance, VendorCreditBalance
# Register your models here.



class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    
    search_fields = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_address', 'vendor_active')

    list_display_links = ('vendor_id', 'vendor_name', 'vendor_type', 'vendor_company', 'vendor_contactNo', 'vendor_alternateNo', 'vendor_address', 'vendor_active', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')




class VendorProductAdmin(admin.ModelAdmin):
    list_display = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds')

    list_display_links = ('vender_product_id', 'vendorId', 'productId', 'product_rate', 'product_tcs', 'product_tds')




class VendorOpeningBalanceAdmin(admin.ModelAdmin):
    list_display = ('vendor_opening_balance_id', 'vendorId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('vendor_opening_balance_id', 'vendorId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    list_display_links = ('vendor_opening_balance_id', 'vendorId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date')




class VendorCreditBalanceAdmin(admin.ModelAdmin):
    list_display = ('vendor_credit_balance_id', 'vendorId', 'amount', 'reason', 'credit_date', 'is_deleted')

    search_fields = ('vendor_credit_balance_id', 'vendorId', 'amount', 'reason', 'credit_date', 'is_deleted')

    list_display_links = ('vendor_credit_balance_id', 'vendorId', 'amount', 'reason', 'credit_date', 'is_deleted')





admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorProduct, VendorProductAdmin)
admin.site.register(VendorOpeningBalance, VendorOpeningBalanceAdmin)
admin.site.register(VendorCreditBalance, VendorCreditBalanceAdmin)