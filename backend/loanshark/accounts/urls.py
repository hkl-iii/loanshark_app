from django.urls import path, include
from .views import  *
from rest_framework import routers
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    
    
]
