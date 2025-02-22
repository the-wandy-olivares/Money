from django.urls import path
from . import views

app_name = "calculator"
urlpatterns = [ 
      path('', views.Calculator.as_view(), name='calculator'),
]