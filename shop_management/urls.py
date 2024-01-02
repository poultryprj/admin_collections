from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),

    path('admin_collections/', include('account.urls')),

    path('route/', include('route.urls')),

    path('shop/', include('shop.urls')),

    path('vehicle/', include('vehicle.urls')),

    path('vendor/', include('vendor.urls')),

    path('api/', include('api.urls')),
    
    path('asset/', include('asset.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

