from django.urls import path
from . import views

app_name = "client"
urlpatterns = [ 
      path('', views.Client.as_view(), name='client'),
]