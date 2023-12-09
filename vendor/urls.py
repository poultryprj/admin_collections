from django.urls import path
from . import views

urlpatterns = [
    path('vendor_list/', views.VendorList, name='vendor_list'),

    path('vendor_add/', views.VendorAdd, name='vendor_add'),

    path('vendor_edit/<int:id>/', views.VendorEdit, name='vendor_edit'),

    path('vendor_delete/<int:id>/', views.VendorDelete, name='vendor_delete'),


    # ================= Vendor Product ==========

    path('vendor_product_add/', views.VendorProductAdd, name='vendor_product_add'),

]
