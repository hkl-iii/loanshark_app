from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib import auth
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    default_error_messages = {
        'password': 'Passwords do not match ',
        'document':'Proof of employment should be uploaded'
    }
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    document = models.FileField(upload_to='images/',null=False, blank=False)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password','document']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')
        document = attrs.get('document', '')
        
        if password != confirm_password:
            raise serializers.ValidationError(self.default_error_messages)
        if not document:
            raise serializers.ValidationError(self.default_error_messages['document'])

        
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')
        document = validated_data.get('document', '')

        return User.objects.create_user(email=email,password=password,document=document)


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password',  'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified and not user.is_staff:
            raise AuthenticationFailed('Account is not verified yet by Admin')
        

        return {
            'email': user.email,
           'tokens': user.tokens
        }

        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'