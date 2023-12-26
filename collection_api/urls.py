from django.urls import path
from .import views

urlpatterns = [

    path('shop_list_api/',views.ShopModelListView, name='shop_list_api'),

    path('collections_api/',views.CollectionsAddView, name='collections_api'),


    # Login Api
    path('user_login_api/', views.UserLogin, name='user_login_api'),


    # Route List
    path('route_list_api/', views.RoutesList, name='route_list_api'),
    

    # Get shop under route
    path('get_shops_under_route_api/<int:route_id>/', views.GetShopsUnderRoute, name='get_shops_under_route_api'),
    path('get_shops_under_route_api/<int:route_id>/<str:shop_code>/', views.GetShopsUnderRoute, name='get_shops_under_route_with_shop_code_api'),
    
################################################################################
    path('collections_view/',views.CollectionView, name='collections_view'),
    path('collection_mode_add/',views.CollectionModeAdd, name='collection_mode_add'),
     path('collection_mode_get/<int:collection_id>/', views.CollectionModeGet, name='collection_mode_get'),



# ******************* 

    path('users/by-group/', views.UserListByGroup, name='user-list-by-group'),

    path('groups/', views.GroupList, name='group-list'),

    path('vehicles/', views.vehicleList, name='vehicle-list'),

    path('received-products/', views.ReceivedProductsByDate, name='received-products-by-date'),

    path('issue-products/', views.IssueProductsByDate, name='issue-products-by-date'),

    path('issue-products_by_date_driver_vehicle/', views.IssueProductsByDateDriverVechicle, name='issue-products_by_date_driver_vehicle/'),
    
]