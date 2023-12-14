from django.urls import path
from . import views

urlpatterns = [

    path('', views.Login, name='Login'),

    path('logout/', views.Logout, name='Logout'),

    path('home/' , views.Index, name='Index'), 

    
]
