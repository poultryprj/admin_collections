from django.urls import path
from . import views

urlpatterns = [

    # Shops Urls
    path('shop_list/', views.ShopList, name='shop_list'),

    path('shop_add/', views.ShopAdd, name='shop_add'),

    path('shop_edit/<int:id>', views.ShopEdit, name='shop_edit'),

    path('shop_update', views.ShopUpdate, name='shop_update'),

    path('shop_delete/<int:id>', views.ShopDelete, name='shop_delete'),


   
    # Shop Owner Urls
    path('shop_owner_list/', views.ShopOwnerList, name='shop_owner_list'),

    path('shop_owner_add/', views.ShopOwnerAdd, name='shop_owner_add'),

    path('shop_owner_edit/<int:id>', views.ShopOwnerEdit, name='shop_owner_edit'),

    path('shop_owner_update/', views.ShopOwnerUpdate, name='shop_owner_update'),

    path('shop_owner_delete/<int:id>', views.ShopOwnerDelete, name='shop_owner_delete'),


    path('shop_routes/', views.RouteList, name='shoproute_list'),
    # path('shop_routes_list/', views.AllShopList, name='shop_routes_list'),

    # path('selected_shops/', views.selected_shops, name='selected_shops'),


]