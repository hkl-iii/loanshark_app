from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import  *


router = DefaultRouter()

urlpatterns = [
    path('auth/login/', LoginAPIView.as_view(), name="login"),

]