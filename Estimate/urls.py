from django.urls import path
from . import views
from .views import EstimateView
urlpatterns = [
    path('',views.EstimateForms,name="EstimateForms"),
    path('EstimateView/',views.EstimateView,name="EstimateView")
    #path("EstimateView/", EstimateView.as_view(), name="EstimateView"),
]
