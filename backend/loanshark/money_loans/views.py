from django.shortcuts import render,redirect
from rest_framework import generics, status, views, permissions
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated, IsAuthenticatedOrReadOnly,AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

class LoansAPIView(generics.GenericAPIView):
    serializer_class = LoansSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    default_error_messages = {
        'amount': 'Amount should be > 100 $ and < 1000 $ ',
        'user_exists':'You need to pay back the total amount before applying again !'
        
    }
    def post(self, request,*args,**kwargs):
        request_data = request.data
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = request_data.get('amount', '')
        user_id = request_data.get('user', '')
        user = get_object_or_404(User,id=user_id)

        if Loans.objects.filter(user=user,is_done=False).exists():
            raise serializers.ValidationError(self.default_error_messages['user_exists'])
        else:   
            if not int(amount) > 100 and  int(amount) < 1000:
                raise serializers.ValidationError(self.default_error_messages['amount'])
            else:
                loan = serializer.save()
                price = loan.calculate_total_amount()
                loan.total_amount_to_pay = price + int(amount)
                loan.remaining_amount_to_pay = price + int(amount)

                loan.save()
                return Response({
                    "msg": "Success",
                    
                },status=status.HTTP_201_CREATED)


def paymentPage(request):
    if Loans.objects.filter(user=request.user,is_done=False).exists():

        loan = Loans.objects.filter(user=request.user,is_done=False).first()
        payback_period = int(loan.payBack_periode)
        if payback_period != 0:
            amount_to_pay = int(loan.total_amount_to_pay) / 3
            
            remaining = int (float(loan.remaining_amount_to_pay))
            context = {
                'loan':loan,
                'amount_to_pay':int(amount_to_pay)
            }
            
            if request.method == 'POST':
                if payback_period != 0:
                    amount = int(loan.total_amount_to_pay) / 3
                    print('testinggggggg')
                    card = stripe.Source.retrieve(request.POST['sourceId'])
                    print('card',card)
                    customer = stripe.Customer.create(
                        email=request.POST['email'],
                        name=request.POST['nickname'],
                        source = card.id
                    )

                    charge = stripe.Charge.create(
                        customer = customer,
                        amount = int(amount)*100 ,
                        currency = 'USD',
                        description="Loan Payment Back"
                    )
                    
                    transaction = remaining - int(amount_to_pay)
                    
                    print('transaction',transaction)
                    
                    Loans.objects.filter(user=request.user,is_done=False).update(remaining_amount_to_pay=int(transaction), payBack_periode=str(payback_period-1))
                    messages.info(request, 'Payment has been done succesfully!')
                
            return render(request, 'payment.html',context)

        elif payback_period == 0:
            Loans.objects.filter(user=request.user,is_done=False).update(is_done=True)
            return redirect('http://localhost:8000/')

    else:
        return redirect('http://localhost:8000/')
