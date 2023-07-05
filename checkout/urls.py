
from django.urls import path
from . import views

urlpatterns = [
    path('',views.CheckoutViews,name="CheckoutViews"),
    path('Payment/',views.Payment,name="Payment"),
    path('invoice/',views.invoice,name="invoice")  
]
