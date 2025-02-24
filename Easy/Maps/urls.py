from django.urls import path
from . import views

app_name = "maps"
urlpatterns = [  
      path('', views.Maps.as_view(), name='maps'),
]