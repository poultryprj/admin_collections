from django.urls import path
from . import views

urlpatterns = [
    path('vehicle_detail_list/', views.VehicleDetailList, name='vehicle_detail_list'),
    path('vehicle_detail_add/', views.VehicleDetailAdd, name='vehicle_detail_add'),

    path('vehicle_make_by_add/', views.vehicle, name='vehicle_make_by_add'),
    
    path('vehicle_detail_edit/<int:id>/', views.VehicleDetailEdit, name='vehicle_detail_edit'),
    
    path('vehicle_detail_update/', views.VehicleDetailsUpdate, name='vehicle_detail_update'),



# ==================================================================================

    


# =====================================Fitness=============================================
    path('vehicle_fitness_add/<int:vehicle_id>/', views.VehicleFitnessAdd, name='vehicle_fitness_add'),
    path('vehicle_fitness_list/', views.VehicleFitnessList, name='vehicle_fitness_list'),
    path('vehicle_fitness_edit/<int:id>/', views.VehicleFitnessEdit, name='vehicle_fitness_edit'),

    path('vehicle_fitness_detail_update/', views.VehicleFitnessDetailsUpdate, name='vehicle_fitness_detail_update'),
    
    path('vehicle_fitness_detail_delete/<int:id>/', views.VehicleFitnessDetailsdelete, name='vehicle_fitness_detail_delete'),

# =========================================Show vehicle all details=========================================
    path('show_vehicle_details/<int:id>/', views.ShowVehicleDetail, name='show_vehicle_details'),

# =========================================Vehicle insurance================================================
    path('vehicle_insurance_add/<int:vehicle_id>/', views.VehicleInsuranceAdd, name='vehicle_insurance_add'),

    path('vehicle_insurance_company_add/', views.VehicleInsuranceCompanyAdd, name='vehicle_insurance_company_add'),  ##dropdown
    path('vehicle_insurance_company_list/', views.VehicleInsuranceCompanyAddList, name='vehicle_insurance_company_list'), ##dropdown

    path('vehicle_insurance_list/', views.VehicleInsuranceList, name='vehicle_insurance_list'),
    path('vehicle_insurance_edit/<int:id>/', views.VehicleInsuranceEdit, name='vehicle_insurance_edit'),
    path('vehicle_insurance_update/', views.vehicleInsuranceUpdate, name='vehicle_insurance_update'),
    path('vehicle_insurance_delete/<int:id>/', views.vehicleInsuranceDelete, name='vehicle_insurance_delete'),

# ======================================= Vehicle Permit ===================================================

    path('vehicle_permit_add/<int:vehicle_id>/', views.VehiclePermitAdd, name='vehicle_permit_add'),
    path('vehicle_permit_list/', views.VehiclePermitList, name='vehicle_permit_list'),
    path('vehicle_permit_edit/<int:id>/', views.VehiclePermitEdit, name='vehicle_permit_edit'),
    path('vehicle_permit_update/', views.vehiclePermitUpdate, name='vehicle_permit_update'),
    path('vehicle_permit_delete/<int:id>/', views.vehiclePermitdelete, name='vehicle_permit_delete'),

# ======================================= Vehicle Pollution =========================================================

    path('vehicle_pollution_add/<int:vehicle_id>/', views.VehiclePollutionAdd, name='vehicle_pollution_add'),
    path('vehicle_pollution_list/', views.VehiclePollutionList, name='vehicle_pollution_list'),
    path('vehicle_pollution_edit/<int:id>/', views.VehiclePollutionEdit, name='vehicle_pollution_edit'),
    path('vehicle_pollution_update/', views.vehiclePollutionUpdate, name='vehicle_pollution_update'),
    path('vehicle_pollution_delete/<int:id>/', views.vehiclePollutiondelete, name='vehicle_pollution_delete'),

# ======================================= Vehicle Tax =========================================================

    path('vehicle_tax_add/<int:vehicle_id>/', views.VehicleTaxAdd, name='vehicle_tax_add'),
    path('vehicle_tax_list/', views.VehicleTaxList, name='vehicle_tax_list'),
    path('vehicle_tax_edit/<int:id>/', views.VehicleTaxEdit, name='vehicle_tax_edit'),
    path('vehicle_tax_update/', views.vehicleTaxUpdate, name='vehicle_tax_update'),
    path('vehicle_tax_delete/<int:id>/', views.vehicleTaxdelete, name='vehicle_tax_delete'),

]



