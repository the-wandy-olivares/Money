# Desc: URL patterns for the app
from django.urls import path, include
from . import views, views_ajax




app_name = "membreship"
urlpatterns = [
      path('', views.Membreship.as_view(), name='membreship'),
                  path('pay-paypal/<int:pk>', views.PaymentPaypal.as_view(),  name='pay-paypal'),
            path('payment-done/', views.PaypalDone.as_view(), name='payment-done'),
      path('payment-canceled/', views.PaypalCaceled.as_view(), name='payment-canceled'),

      # Ajax
      path('ajax/create-pay/', views_ajax.CreatePay, name='create-pay'),

]                 