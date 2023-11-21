from django.urls import path
from . import views

urlpatterns = [

    path('user_list/', views.UserList, name='user_list'),

    path('add_user/', views.AddUser, name='add_user'),

    path('edit_user/<int:id>', views.EditUser, name='edit_user'),

    path('user_update/', views.UserUpdate, name='user_update'),

    path('user_delete/<int:id>/', views.UserDelete, name='user_delete'),

]
