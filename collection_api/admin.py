from django.contrib import admin


from .models import Collection, CollectionMode

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collection_id', 'collection_date', 'collection_time', 'shopId', 'cashierId', 'total_amount')
    list_filter = ('collection_date', 'shopId', 'cashierId')
    search_fields = ('collection_id', 'total_amount', 'cashierId__username')  # Add fields for search


class CollectionModeAdmin(admin.ModelAdmin):
    list_display = ('collection_mode_id', 'payment_mode', 'payment_amount', 'upload_image')
    list_filter = ('collection_mode_id', 'payment_mode', 'payment_amount', 'upload_image')
    search_fields = ('collection_mode_id', 'payment_mode', 'payment_amount', 'upload_image')  # Add fields for search



admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionMode, CollectionModeAdmin)
