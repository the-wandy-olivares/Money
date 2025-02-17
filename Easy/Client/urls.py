from django.urls import path
from . import views

app_name = "client"
urlpatterns = [ 
      path('', views.Client.as_view(), name='client'),
            path('create/', views.ClientCreate.as_view(), name='client-create'),
                  path('update/<int:pk>/', views.ClientUpdate.as_view(), name='client-update'),
                  path('detail/<int:pk>/', views.ClientDetail.as_view(), name='client-detail'),
            path('list/', views.ClientList.as_view(), name='client-list'),
      path('delete/<int:pk>/', views.ClientDelete.as_view(), name='client-delete'),
]