from django.urls import path
from .import views

urlpatterns = [
    path('asset_add/', views.AssetAdd, name='asset_add'),
    path('asset_list/', views.AssetList, name='asset_list'),
    path('asset_edit/<int:id>/', views.AssetEdit, name='asset_edit'),
    path('asset_update/', views.AssetUpdate, name='asset_update'),
    path('asset_delete/<int:id>/', views.Assetdelete, name='asset_delete'),

]
