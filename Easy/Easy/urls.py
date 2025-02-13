# Version: 1.0
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard

urlpatterns = [
        path('', Dashboard.as_view(), name='dashboard'),
        path('company/', include('Company.urls')),  #Empresas
        path('client/', include('Client.urls')),  #Clientes
        path('admin/', admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
