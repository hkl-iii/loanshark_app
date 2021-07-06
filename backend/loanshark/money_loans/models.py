from django.db import models
from accounts.models import User

# Create your models here.

class Loans(models.Model):
    default_type = '3'
    payback = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    amount = models.CharField(max_length=30, blank=True, null=True)
    total_amount_to_pay = models.CharField(max_length=30, blank=True, null=True)
    remaining_amount_to_pay = models.CharField(max_length=30, blank=True, null=True)
    payBack_periode = models.CharField(max_length=50,choices=payback,default=default_type,blank=True, null=True)
    is_verified = models.BooleanField(default=True)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.user.email)

    def calculate_total_amount(self):
        amount = int(self.amount)
        total = int((amount * 30) / 100)
        return total

    class Meta:
        verbose_name_plural = 'Loans'
