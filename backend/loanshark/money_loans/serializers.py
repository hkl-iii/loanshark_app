from rest_framework import serializers
from .models import *
from rest_framework import generics, status, views, permissions
from rest_framework.response import Response



class LoansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loans
        fields = ['user','amount']



        
