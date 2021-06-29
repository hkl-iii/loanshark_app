from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from money_loans.models import *
from django.core import serializers
# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    def post(self, request):
        user = request.data
        # serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        email = user.get('email', '')
        password = user.get('password', '')
        proof = user.get('proof', '')
        full_name = user.get('full_name', '')
        phone_number = user.get('phone_number', '')
        User.objects.create_user(email=email,password=password,proof=proof,full_name=full_name,phone_number=phone_number)

        # if 'proof' in serializer.validated_data:
        #     proof = serializer.validated_data.pop('proof')
        #     email = user.get('email', '')
        #     password = user.get('password', '')
        #     proof = user.get('proof', '')
            
        #     print('views_proof',proof)
        #     user = serializer.save()
        #     user.proof = proof
        #     user.save()
        # serializer.save()
        
        # user_data = serializer.data

        return Response( status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (
        permissions.AllowAny,
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('serializer.data',serializer.data)
        user = serializer.validated_data
        # print('user',user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

