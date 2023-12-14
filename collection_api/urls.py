from django.urls import path
from . import views

urlpatterns = [

    path('shop_list_api/',views.ShopModelListView, name='shop_list_api'),

    path('collections_api/',views.CollectionsAddView, name='collections_api'),
    
]