# Desc: URL patterns for the app
from django.urls import path
from .views import Caja

app_name = "caja"
urlpatterns = [
      path('', Caja.as_view(), name='caja'),
]