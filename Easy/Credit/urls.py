from django.urls import path
from . import views

app_name = "credit"
urlpatterns = [  
      path('', views.Credit.as_view(), name='credit'),
            path('create/', views.CreditCreate.as_view(), name='credit-create'),
                  path('update/<int:pk>/', views.CreditUpdate.as_view(), name='credit-update'),
                        path('detail/<int:pk>/', views.CreditDetail.as_view(), name='credit-detail'),
                  path('list/', views.CreditList.as_view(), name='credit-list'),
            path('delete/<int:pk>/', views.CreditDelete.as_view(), name='credit-delete'),
]