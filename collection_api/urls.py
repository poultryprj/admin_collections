from django.urls import path
from .import views

urlpatterns = [

    path('shop_list_api/',views.ShopModelListView, name='shop_list_api'),

    path('collections_api/',views.CollectionsAddView, name='collections_api'),


    # Login Api
    path('user_login_api/', views.UserLogin, name='user_login_api'),


    # Route List
    path('route_list_api/', views.RoutesList, name='route_list_api'),\
    

    # Get shop under route
    path('get_shops_under_route_api/<int:route_id>/', views.GetShopsUnderRoute, name='get_shops_under_route_api'),
    
################################################################################
    path('collections_view/',views.CollectionView, name='collections_view'),
    path('collection_mode_add/',views.CollectionModeAdd, name='collection_mode_add'),
    path('collection_mode_get/<int:collection_id>/', views.CollectionModeGet, name='collection_mode_get'),

#################################### Skip Shop ############################################
     
    path('skip_shop_add/', views.SkipShopAdd, name="skip_shop_add"),
    path('skip_shop_view/', views.SkipShopListView, name="skip_shop_view"),

#################################### Complaint ############################################

    path('complaint_add/', views.ComplaintAdd, name="complaint_add"),
    path('complaint_view/', views.ComplaintListView, name="complaint_view")
    
]

