# Version: 1.0
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard, Logout

urlpatterns = [
        path('', Dashboard.as_view(), name='dashboard'),
                path('company/', include('Company.urls')),  #Empresas
                        path('client/', include('Client.urls')),  #Clientes
                                path('credit/', include('Credit.urls')), # Creditos 
                                        path('calculator/', include('Calculator.urls')), # Calculadora
                                path('maps/', include('Maps.urls')), # Mapas
                        path('agenda/', include('Agenda.urls')), # Agenda
                path('caja/', include('Caja.urls')), # Caja
        path('mensajes/', include('Mensajeria.urls')), # Mensajes
                path('perfil/', include('Perfil.urls')), # Perfil
                        path('login', include('Login.urls')), # Login
                                path('inversion/', include('Inversion.urls')), # Inversion
                                         path('asistente/', include('Asistente.urls')), # Asistente
                                path('admin/', admin.site.urls), # Aministracion
                                path('logout/', Logout, name='logout'), # Logout

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
