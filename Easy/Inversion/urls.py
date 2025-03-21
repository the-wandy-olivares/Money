# Desc: URL patterns for the app
from django.urls import path
from . import views


app_name = "inversion"
urlpatterns = [
      path('', views.Inversion.as_view(), name='inversion'),


]