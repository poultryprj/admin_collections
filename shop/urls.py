from django.urls import path
from . import views

urlpatterns = [

    # Shops Urls
    path('shop_list/', views.ShopList, name='shop_list'),
    path('ShopBalanceDetails/<int:id>', views.ShopBalanceDetails, name='ShopBalanceDetails'),

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


    # Shop Routes Urls
    path('shop_routes/', views.ShopRouteList, name='shoproute_list'),

    

    # Product Type Urls
    path('product_types/', views.ProductTypeList, name='product_type'), 

    path('product_type_add/', views.ProductTypeAdd, name='product_type_add'),

    path('product_type_edit/<int:id>/', views.ProductTypeEdit, name='product_type_edit'),


    # Product Category Urls
    path('product_categories/', views.ProductCategoriesList, name='product_categories'),

    path('product_category_add/', views.ProductCategoriesAdd, name='product_categories_add'),

    path('product_category_edit/<int:id>/', views.ProductTypeUpdate, name='product_category_edit'),


    # Product Master Urls
    path('product_list/', views.ProductList, name='product_list'), 

    path('product_add/', views.ProductAdd, name='product_add'),

    path('product_edit/<int:id>', views.ProductEdit, name='product_edit'),

    path('product_update/', views.ProductUpdate, name='product_update'),

    path('product_delete/<int:id>', views.ProductDelete, name='product_delete'),



    # Product Rate Urls
    path('product_rate_list/', views.ProductRateList, name='product_rate_list'), 

    path('product_rate_add/', views.ProductRateAdd, name='product_rate_add'),

    path('product_rate_edit/<int:id>/', views.ProductRateEdit, name='product_rate_edit'),

    path('product_rate_update/', views.ProductRateUpdate, name='product_rate_update'),

    path('product_rate_delete/<int:id>/', views.ProductRateDelete, name='product_rate_delete'),



    #  Shop Balance
    path('shop_balance_list/', views.ShopBalanceList, name='shop_balance_list'),

    path('shop_balance_add/', views.ShopBalanceAdd, name='shop_balance_add'),

    path('shop_balance_edit/<int:id>', views.ShopBalanceEdit, name='shop_balance_edit'),

    path('shop_balance_delete/<int:id>', views.ShopBalanceDelete, name='shop_balance_delete'),


    path('shop_and_balance_detail/<int:id>', views.ShopAndBalanceDetail, name='shop_and_balance_detail'),



    # Shop Flexible Rate
    path('shop_flexible_rate_list/', views.ShopFlexibleRateList, name='shop_flexible_rate_list'),

    path('shop_flexible_rate_add/', views.ShopFlexibleRateAdd, name='shop_flexible_rate_add'),

    path('shop_flexible_rate_edit/<int:id>', views.ShopFlexibleRateEdit, name='shop_flexible_rate_edit'),

    path('shop_flexible_rate_delete/<int:id>', views.ShopFlexibleRateDelete, name='shop_flexible_rate_delete'),


    
]