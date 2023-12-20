from django.contrib import admin
from asset.models import AssetPurchase, Assets, AssetDistribution

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ( 'asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    list_display_links = ('asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    

class AssetPurchaseAdmin(admin.ModelAdmin):
    list_display = (
        'asset_purchase_id', 'purchase_on', 'vendor_Id', 'asset_Id', 'quantity', 
        'weight', 'rate', 'amount', 'remarks', 'created_on', 'created_by', 
        'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by'
    )
    search_fields = (
        'asset_purchase_id', 'purchase_on', 'quantity', 
        'weight', 'rate', 'amount', 'remarks', 'created_on', 'created_by', 
        'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by'
    )
    list_display_links = (
        'asset_purchase_id', 'purchase_on', 'quantity', 
        'weight', 'rate', 'amount', 'remarks', 'created_on', 'created_by', 
        'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by'
    )

class AssetDistributionAdmin(admin.ModelAdmin):
    list_display = (
        'asset_distribution_id', 'distribution_date_and_time', 'assets_consumer_type', 
        'user_group', 'distribution_to_id', 'quantity', 'weight', 'remarks', 
        'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 
        'is_deleted', 'deleted_by'
    )
    search_fields = (
        'asset_distribution_id', 'distribution_date_and_time', 'assets_consumer_type', 
        'user_group__name', 'distribution_to_id', 'quantity', 'weight', 'remarks', 
        'created_on', 'created_by__username', 'last_modified_on', 'last_modified_by__username', 
        'is_deleted', 'deleted_by__username'
    )
    list_display_links = (
        'asset_distribution_id', 'distribution_date_and_time', 'assets_consumer_type', 
        'user_group', 'distribution_to_id', 'quantity', 'weight', 'remarks', 
        'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 
        'is_deleted', 'deleted_by'
    )


admin.site.register(Assets,AssetAdmin)
admin.site.register(AssetPurchase,AssetPurchaseAdmin)
admin.site.register(AssetDistribution, AssetDistributionAdmin)