from django.urls import path
from . import views

app_name = "published"
urlpatterns = [  
      path('', views.Published.as_view(), name='published'),
]