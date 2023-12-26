from django.contrib import admin
from .models import ProductIssue, ProductRecieve, ShopBalance, ShopFlexibleRate, ShopModel, ShopOwner, ShopRoute, ProductTypes, ProductCategories, ProductMaster, Associations, ShopProductRates



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





class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('product_type_id', 'product_type')

    search_fields = ('product_type_id','product_type')

    list_display_links = ('product_type_id','product_type')




class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_id', 'product_category')

    search_fields = ('product_category_id','product_category')

    list_display_links = ('product_category_id','product_category')


class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_typeId', 'product_categoryId', 'product_value_on', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('product_id','product_name', 'product_typeId', 'product_categoryId', 'product_value_on' )

    list_display_links = ('product_id','product_name', 'product_typeId', 'product_categoryId', 'product_value_on')



class AssociationsAdmin(admin.ModelAdmin):
    list_display = ('association_id', 'association_name', 'association_sequence')

    search_fields = ('association_id','association_name', 'association_sequence' )

    list_display_links = ('association_id','association_name', 'association_sequence')


class ShopProductRatesAdmin(admin.ModelAdmin):
    list_display = ('shop_product_rates_id', 'shopId', 'associationId', 'ProductId', 'rate_margin', 'flexible_yn', 'flexible_formula', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('shop_product_rates_id','shopId', 'associationId', 'ProductId' )

    list_display_links = ('shop_product_rates_id','shopId', 'associationId', 'ProductId', 'rate_margin')




class ShopBalanceAdmin(admin.ModelAdmin):
    list_display = ('shop_balance_id', 'shopId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date')

    search_fields = ('shop_balance_id', 'shopId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date')

    list_display_links = ('shop_balance_id', 'shopId', 'balance_date', 'balance', 'active', 'adjustment_amount', 'adjustment_remark', 'balance_utc_date')



class ShopFlexibleRateAdmin(admin.ModelAdmin):
    list_display = ('shop_flexible_rate_id', 'flexible_rate_date', 'shopId', 'product_typeId', 'flexible_rate', 'flexible_formula', 'sell_rate', 'with_skin', 'without_skin', 'sms_send_yn', 'sms_replyId', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('shop_flexible_rate_id', 'flexible_rate_date', 'shopId', 'product_typeId', 'flexible_rate', 'flexible_formula', 'sell_rate', 'with_skin', 'without_skin', 'sms_send_yn', 'sms_replyId' )

    list_display_links = ('shop_flexible_rate_id', 'flexible_rate_date', 'shopId', 'product_typeId', 'flexible_rate', 'flexible_formula', 'sell_rate', 'with_skin', 'without_skin', 'sms_send_yn', 'sms_replyId')



class ProductRecieveModelAdmin(admin.ModelAdmin):
    list_display = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')

    search_fields = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId')

    list_display_links = ('product_record_id', 'recieved_date', 'vendorId', 'product_typeId', 'productId','paper_rate', 'amount', 'recieved_amount', 'vehicleId', 'driverId', 'delete_reason')



class ProductIssueAdmin(admin.ModelAdmin):
    list_display = ('product_issue_id', 'issue_date', 'shopId', 'paper_rate', 'boiler_size', 'issue_birds', 'birds_weight', 'daily_rate', 'issue_amount', 'vehicleId', 'driverId','entry_source', 'latitude', 'longtitude', 'product_typeId', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ('product_issue_id', 'issue_date', 'shopId', 'paper_rate', 'boiler_size', 'issue_birds', 'birds_weight', 'daily_rate', 'issue_amount', 'vehicleId', 'driverId','entry_source', 'latitude', 'longtitude', 'product_typeId', 'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    list_display_links = ('product_issue_id', 'issue_date', 'shopId', 'paper_rate', 'boiler_size', 'issue_birds', 'birds_weight', 'daily_rate', 'issue_amount', 'vehicleId', 'driverId','entry_source', 'latitude', 'longtitude', 'product_typeId')




admin.site.register(ShopOwner, ShopOwnerModelAdmin)
admin.site.register(ShopModel,ShopModelAdmin)
admin.site.register(ShopRoute,ShopRouteAdmin)
admin.site.register(ProductTypes,ProductTypeAdmin)
admin.site.register(ProductCategories,ProductCategoryAdmin)
admin.site.register(ProductMaster,ProductMasterAdmin)
admin.site.register(Associations,AssociationsAdmin)
admin.site.register(ShopProductRates,ShopProductRatesAdmin)
admin.site.register(ShopBalance,ShopBalanceAdmin)
admin.site.register(ShopFlexibleRate,ShopFlexibleRateAdmin)
admin.site.register(ProductRecieve,ProductRecieveModelAdmin)
admin.site.register(ProductIssue,ProductIssueAdmin)
