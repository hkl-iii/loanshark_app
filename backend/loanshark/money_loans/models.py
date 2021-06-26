from django.db import models
from accounts.models import User

# Create your models here.

class Loans(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    amount = models.CharField(max_length=30, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.user.email)

    class Meta:
        verbose_name_plural = 'Loans'
