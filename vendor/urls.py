from django.urls import path
from . import views

urlpatterns = [
    path('vendor_list/', views.VendorList, name='vendor_list'),

    path('vendor_add/', views.VendorAdd, name='vendor_add'),

    path('vendor_edit/<int:id>/', views.VendorEdit, name='vendor_edit'),

    path('vendor_delete/<int:id>/', views.VendorDelete, name='vendor_delete'),


    # ================= Vendor Product ==========

    path('vendor_product_list/', views.VendorProductList, name='vendor_product_list'),

    path('vendor_product_add/', views.VendorProductAdd, name='vendor_product_add'),

    path('vendor_product_edit/<int:id>', views.VendorProductEdit, name='vendor_product_edit'),

    path('vendor_product_delete/<int:id>', views.VendorProductDelete, name='vendor_product_delete'),


    # ============================= Vendor Opening Balance ================================

    path('vendor_opening_balance_list/', views.VendorOpeningBalanceList, name='vendor_opening_balance_list'),

    path('vendor_opening_balance_add/', views.VendorOpeningBalanceAdd, name='vendor_opening_balance_add'),

    path('vendor_opening_balance_edit/<int:id>', views.VendorOpeningBalanceEdit, name='vendor_opening_balance_edit'),

    path('vendor_opening_balance_delete/<int:id>', views.VendorOpeningBalanceDelete, name='vendor_opening_balance_delete'),


    # ================================== Vendor Credit Balance =====================================

    path('vendor_credit_balance_list/', views.VendorCreditBalanceList, name='vendor_credit_balance_list'),

    path('vendor_credit_balance_add/', views.VendorCreditBalanceAdd, name='vendor_credit_balance_add'),

    path('vendor_credit_balance_edit/<int:id>', views.VendorCreditBalanceEdit, name='vendor_credit_balance_edit'),

    path('vendor_credit_balance_delete/<int:id>', views.VendorCreditBalanceDelete, name='vendor_credit_balance_delete'),

]
