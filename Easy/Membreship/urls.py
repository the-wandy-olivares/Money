# Desc: URL patterns for the app
from django.urls import path
from . import views


app_name = "membreship"
urlpatterns = [
      path('', views.Membreship.as_view(), name='membreship'),
]