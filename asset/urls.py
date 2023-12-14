from django.urls import path
from .import views

urlpatterns = [
    path('asset_add/', views.AssetAdd, name='asset_add'),
    path('asset_list', views.AssetList, name='asset_List'),


]
