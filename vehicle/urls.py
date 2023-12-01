from django.urls import path
from . import views

urlpatterns = [
    path('vehicle_detail_add/', views.VehicleDetailAdd, name='vehicle_detail_add'),
    path('vehicle_make_by_add/', views.vehicalMakeByAdd, name='vehicle_make_by_add'),
]
