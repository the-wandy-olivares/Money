# Desc: URL patterns for the app
from django.urls import path
from . import views

app_name = "company"
urlpatterns = [
      path('company-update/<int:pk>', views.CompanyUpdate.as_view(), name='company-update'),
]