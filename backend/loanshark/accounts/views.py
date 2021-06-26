from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from .serializers import *
from rest_framework.response import Response

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


