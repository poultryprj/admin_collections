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
    
################################################################################
    path('collections_view/',views.CollectionView, name='collections_view'),

    
    path('collection_mode_add/',views.CollectionModeAdd, name='collection_mode_add'),
    path('otp_verification/', views.OTPVerification, name='otp_verification'),

    path('collection_mode_get/<int:collection_id>/', views.CollectionModeGet, name='collection_mode_get'),



# ******************* 

    path('users_by-group_api/', views.UserListByGroup, name='user-list-by-group'),

    path('groups_api/', views.GroupList, name='group-list'),

    path('vehicles_api/', views.vehicleList, name='vehicle-list'),

    path('received-products_api/', views.ReceivedProductsByDate, name='received-products-by-date'),

    path('issue-products_api/', views.IssueProductsByDate, name='issue-products-by-date'),

    path('issue-products_by_date_driver_vehicle_api/', views.IssueProductsByDateDriverVechicle, name='issue-products_by_date_driver_vehicle/'),

    #################################### Skip Shop ############################################
     
    path('skip_shop_add/', views.SkipShopAdd, name="skip_shop_add"),

    path('skip_shop_view/', views.SkipShopListView, name="skip_shop_view"),

#################################### Complaint ############################################

    path('complaint_add/', views.ComplaintAdd, name="complaint_add"),

    path('complaint_view/', views.ComplaintListView, name="complaint_view"),

    path('approve_collection_api/', views.ApproveCollection, name='approve_collection'),  

    path('get_shop_collections_mode_api/', views.GetShopCollections, name='get_shop_collections_mode'),


    #  Add Product Recieve API's
    path('add_product_recieve_api/', views.AddProductReceive, name='add_product_recieve'),

    #  Add Product Issue API's
    path('add_product_issue_api/', views.AddProductIssue, name='add_product_issue'),

    #  Add Vehicle Running API's
    path('add_vehicle_running_api/', views.AddVehicleRunning, name='add_vehicle_running'),

################################### Shop App API ###########################################
    path('create_shop_product_request/', views.CreateShopProductRequest, name="create_shop_product_request"),
    path('product_issues/', views.GetProductIssuesByDate, name='product_issues'),
]




