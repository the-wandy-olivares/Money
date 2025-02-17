from django.urls import path
from . import views

app_name = "credit"
urlpatterns = [  
      path('', views.Credit.as_view(), name='credit'),
]