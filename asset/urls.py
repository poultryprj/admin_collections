from django.urls import path
from .import views

urlpatterns = [
################################################ ASSET ######################################################### 
    path('asset_add/', views.AssetAdd, name='asset_add'),
    path('asset_list/', views.AssetList, name='asset_list'),
    path('asset_edit/<int:id>/', views.AssetEdit, name='asset_edit'),
    path('asset_update/', views.AssetUpdate, name='asset_update'),
    path('asset_delete/<int:id>/', views.AssetDelete, name='asset_delete'),

################################################ ASSET PURCHASE ################################################
    path('asset_purchase_add/', views.AssetPurchaseAdd, name='asset_purchase_add'),
    path('asset_purchase_list/', views.AssetPurchaseList, name='asset_purchase_list'),
    path('asset_purchase_edit/<int:id>/', views.AssetPurchaseEdit, name='asset_purchase_edit'),
    path('asset_purchase_update/', views.AssetPurchaseUpdate, name='asset_purchase_update'),
    path('asset_purchase_delete/<int:id>/', views.AssetPurchaseDelete, name='asset_purchase_delete'),

################################################ ASSET DISTRIBUTIONS ################################################
    path('asset_distribution_add/', views.AssetDistributionAdd, name='asset_distribution_add'),
    path('asset_distribution_list/', views.AssetDistributionList, name='asset_distribution_list'),
    path('asset_distribution_edit/<int:id>/', views.AssetDistributionEdit, name='asset_distribution_edit'),
    path('asset_distribution_update/', views.AssetDistributionUpdate, name='asset_distribution_update'),
    path('asset_distribution_delete/<int:id>/', views.AssetDistributionDelete, name='asset_distribution_delete'),


]
