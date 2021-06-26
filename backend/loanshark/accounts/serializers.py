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
        'password': 'Passwords do not match '
    }
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)
    confirm_password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')

        if password != confirm_password:
            raise serializers.ValidationError(self.default_error_messages)
        
        return attrs

    def create(self, validated_data):
        print('validated_data',validated_data)
        email = validated_data.get('email', '')
        password = validated_data.get('password', '')
        return User.objects.create_user(email=email,password=password)


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