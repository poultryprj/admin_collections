from django.urls import path
from . import views

urlpatterns = [

    path('route_list/', views.RouteList, name='route_list'),

    path('route_add/', views.RouteAdd, name='route_add'),

    path('route_edit/<int:id>', views.RouteEdit, name='route_edit'),

    path('route_update', views.RouteUpdate, name='route_update'),

    path('route_delete/<int:id>', views.RouteDelete, name='route_delete'),


]