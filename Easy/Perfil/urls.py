from django.urls import path
from .views import Perfil

app_name = "perfil"
urlpatterns = [  
      path('', Perfil.as_view(), name='perfil'),
]