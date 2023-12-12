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
    
    path('product_received_edit/<int:id>/', views.ProductReceivedEdit, name='product_received_edit'),
    path('product_received_update/', views.ProductReceivedUpdate, name='product_received_update'),
    
    path('product_received_delete/<int:id>/', views.product_received_delete, name='product_received_delete'),

# =====================================Fitness=============================================
    path('vehicle_fitness_add/', views.VehicleFitnessAdd, name='vehicle_fitness_add'),
    path('vehicle_fitness_list/', views.VehicleFitnessList, name='vehicle_fitness_list'),
    path('vehicle_fitness_edit/<int:id>/', views.VehicleFitnessEdit, name='vehicle_fitness_edit'),

    path('vehicle_fitness_detail_update/', views.VehicleFitnessDetailsUpdate, name='vehicle_fitness_detail_update'),
    
    path('vehicle_fitness_detail_delete/<int:id>/', views.VehicleFitnessDetailsdelete, name='vehicle_fitness_detail_delete'),

# =========================================Show vehicle all details=========================================
    path('show_vehicle_details/<int:id>/', views.ShowVehicleDetail, name='show_vehicle_details'),

# =========================================Vehicle insurance================================================
    path('vehicle_insurance_add/', views.VehicleInsuranceAdd, name='vehicle_insurance_add'),

    path('vehicle_insurance_company_add/', views.VehicleInsuranceCompanyAdd, name='vehicle_insurance_company_add'),  ##dropdown
    path('vehicle_insurance_company_list/', views.VehicleInsuranceCompanyAddList, name='vehicle_insurance_company_list'), ##dropdown

    path('vehicle_insurance_list/', views.VehicleInsuranceList, name='vehicle_insurance_list'),
    path('vehicle_insurance_edit/<int:id>/', views.VehicleInsuranceEdit, name='vehicle_insurance_edit'),
    path('vehicle_insurance_update/', views.vehicleInsuranceUpdate, name='vehicle_insurance_update'),
    path('vehicle_insurance_delete/<int:id>/', views.vehicleInsuranceDelete, name='vehicle_insurance_delete'),

# ======================================= Vehicle Permit ===================================================

    path('vehicle_permit_add/', views.VehiclePermitAdd, name='vehicle_permit_add'),
    path('vehicle_permit_list/', views.VehiclePermitList, name='vehicle_permit_list'),
    path('vehicle_permit_edit/<int:id>/', views.VehiclePermitEdit, name='vehicle_permit_edit'),
    path('vehicle_permit_update/', views.vehiclePermitUpdate, name='vehicle_permit_update'),
    path('vehicle_permit_delete/<int:id>/', views.vehiclePermitdelete, name='vehicle_permit_delete'),

# ======================================= =========================================================

    path('vehicle_pollution_add/', views.VehiclePollutionAdd, name='vehicle_pollution_add'),
    path('vehicle_pollution_list/', views.VehiclePollutionList, name='vehicle_pollution_list'),
    path('vehicle_pollution_edit/<int:id>/', views.VehiclePollutionEdit, name='vehicle_pollution_edit'),
    path('vehicle_pollution_update/', views.vehiclePollutionUpdate, name='vehicle_pollution_update'),
    path('vehicle_pollution_delete/<int:id>/', views.vehiclePollutiondelete, name='vehicle_pollution_delete'),

]



