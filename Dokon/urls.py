from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls')),
    path('panels/admin/',admin.site.urls),
    path('', include('asosiy.urls')),
    path('user/', include('userapp.urls')),
    path('buyurtma/', include('buyurtma.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

