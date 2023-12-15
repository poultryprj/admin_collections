from django.urls import path
from .import views

urlpatterns = [

    path('shop_list_api/',views.ShopModelListView, name='shop_list_api'),

    path('collections_api/',views.CollectionsAddView, name='collections_api'),

################################################################################
    path('collections_view/',views.CollectionView, name='collections_view'),
    path('collection_mode_add/',views.CollectionModeAdd, name='collection_mode_add'),
    
]