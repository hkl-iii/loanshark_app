from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager,AbstractBaseUser
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.

class UserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for authorization
    instead of usernames. The default that's used is "UserManager"
    """

    def _create_user(self, email, password, staff=None, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        if staff:
            user = self.model(email=email, is_staff=True, is_superuser=True, **extra_fields)
        else:
            user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password,
                                 **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        staff = True
        return self._create_user(email, password, staff, **extra_fields)



class User(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    password = models.CharField(max_length=400)
    is_staff = models.BooleanField(default=False)
    document = models.FileField(upload_to='images/',null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    objects = UserManager()


    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True,upload_to='images/')
    address = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.user.email)

    class Meta:
        verbose_name_plural = 'Profile'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'],
        )
post_save.connect(create_profile, sender=User)
