from django.urls import path
from . import views

urlpatterns = [
    path('vehicle_detail_list/', views.VehicleDetailList, name='vehicle_detail_list'),
    path('vehicle_detail_add/', views.VehicleDetailAdd, name='vehicle_detail_add'),

    path('vehicle_make_by_add/', views.vehicle, name='vehicle_make_by_add'),
    
    path('vehicle_detail_edit/<int:id>/', views.VehicleDetailEdit, name='vehicle_detail_edit'),
    
    path('vehicle_detail_update/', views.VehicleDetailsUpdate, name='vehicle_detail_update'),
]
