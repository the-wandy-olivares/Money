# Desc: URL patterns for the app
from django.urls import path
from .views import Mensajeria

app_name = "mensajeria"
urlpatterns = [
      path('', Mensajeria.as_view(), name='mensajeria'),
]