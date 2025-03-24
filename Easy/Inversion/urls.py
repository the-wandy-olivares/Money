# Desc: URL patterns for the app
from django.urls import path
from . import views


app_name = "inversion"
urlpatterns = [
      path('', views.Inversion.as_view(), name='inversion'),
            path('create/', views.InversionCreate.as_view(),  name='inversion-create'),
                  path('update/<int:pk>/', views.InversionUpdate.as_view(), name='inversion-update'),
            path('inversion-agregar-fondos/<int:pk>', views.InversionAgregarFondos.as_view(), name='inversion-agregar-fondos'),
]