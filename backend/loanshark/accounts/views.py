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
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        if 'proof' in serializer.validated_data:
            proof = serializer.validated_data.pop('proof')
            print('views_proof',proof)
            user = serializer.save()
            user.proof = proof
            user.save()
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


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)



# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     #permission_classes = [IsAuthenticatedOrReadOnly]

class ProfileViewSet(generics.GenericAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request,**kwargs):
        email = self.request.query_params.get('email', None)        
        if User.objects.filter(email=email).exists():
            user = get_object_or_404(User, email=email)
        if Profile.objects.filter(user=user).exists():
            profile = get_object_or_404(Profile, user=user)
            full_name = profile.full_name
            phone_number = profile.phone_number
            profile_picture = profile.profile_picture
            address = profile.address
        
        if Loans.objects.all().filter(user=user).exists():
            loans_list = Loans.objects.all().filter(user=user)

        loans_data= serializers.serialize("json", loans_list)
        return Response(
            {
                'email': email,
                'full_name':full_name,
                'phone_number':phone_number,
                #'profile_picture':profile_picture,
                'address':address,
                'loans_list':loans_data
                

            },
            status=status.HTTP_200_OK)
