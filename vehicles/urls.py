from django.urls import path
from . import views

urlpatterns = [
    path('vehicle_detail_list/', views.VehicleDetailList, name='vehicle_detail_list'),
    path('vehicle_detail_add/', views.VehicleDetailAdd, name='vehicle_detail_add'),

    path('vehicle_make_by_add/', views.vehicle, name='vehicle_make_by_add'),
    
    path('vehicle_detail_edit/<int:id>/', views.VehicleDetailEdit, name='vehicle_detail_edit'),
    
    path('vehicle_detail_update/', views.VehicleDetailsUpdate, name='vehicle_detail_update'),



# ==================================================================================

    
    path('product_received_list/', views.ProductReceivedList, name='product_received_list'),

    path('product_received_add/', views.ProductReceivedAdd, name='product_received_add'),
    
    path('product_received_edit/<int:id>', views.ProductReceivedEdit, name='product_received_edit'),
    path('product_received_update/', views.ProductReceivedUpdate, name='product_received_update'),
    
    path('product_received_delete/<int:id>/', views.product_received_delete, name='product_received_delete'),

# ==================================================================================
    path('vehicle_fitness_add', views.VehicleFitnessAdd, name='vehicle_fitness_add'),
    path('vehicle_fitness_list/', views.VehicleFitnessList, name='vehicle_fitness_list'),
    path('vehicle_fitness_edit/<int:id>/', views.VehicleFitnessEdit, name='vehicle_fitness_edit'),

    path('vehicle_fitness_detail_update/', views.VehicleFitnessDetailsUpdate, name='vehicle_fitness_detail_update'),
    
    path('vehicle_fitness_detail_delete/<int:id>/', views.VehicleFitnessDetailsdelete, name='vehicle_fitness_detail_delete'),


    

]



