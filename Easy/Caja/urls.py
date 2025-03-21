# Desc: URL patterns for the app
from django.urls import path
from .views import Caja
from .views_ajax import SearchMove

app_name = "caja"
urlpatterns = [
      path('', Caja.as_view(), name='caja'),

      path('ajax/search-move/', SearchMove, name='search-move'),
]