from django.urls import path, include

from .views import  *

from rest_framework import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('request-loans/', LoansAPIView.as_view(), name="loans"),

    
    


]
