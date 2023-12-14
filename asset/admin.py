from django.contrib import admin
from asset.models import Assets

class AssetAdmin(admin.ModelAdmin):
    list_display = ('asset_id', 'asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    search_fields = ( 'asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')

    list_display_links = ('asset_name', 'asset_types', 'slowly_finished_product', 'long_lasting_products',
                     'created_on', 'created_by', 'last_modified_on', 'last_modified_by', 'is_deleted', 'deleted_by')
    

admin.site.register(Assets,AssetAdmin)