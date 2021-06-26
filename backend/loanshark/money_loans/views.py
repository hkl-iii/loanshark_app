from django.shortcuts import render
from rest_framework import generics, status, views, permissions
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.



class LoansAPIView(generics.GenericAPIView):
    serializer_class = LoansSerializer
    permission_classes = (permissions.AllowAny,)
    
    default_error_messages = {
        'amount': 'Amount should be > 100$ and < 1000$ ',
        
    }
    def post(self, request,*args,**kwargs):
        request_data = request.data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = request_data.get('amount', '')
        user = request_data.get('user', '')
        
        
        if not int(amount) > 100 and  int(amount) < 1000:
            raise serializers.ValidationError(self.default_error_messages['amount'])


        else:
            serializer.save()  
            return Response({
                "msg": "Success",
                
            },status=status.HTTP_201_CREATED)

