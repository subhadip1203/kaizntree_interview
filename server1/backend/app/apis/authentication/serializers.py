
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import EmailVerification , PasswordResetToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True, 'required': True}, 'username': {'required': False}}

    def create(self, validated_data):
        #Set the username to the email address
        validated_data['username'] = validated_data['email']
        user = User.objects.create_user(**validated_data)
        return user

class EmailVerificationSerializer(serializers.Serializer):
    token = serializers.UUIDField()

    def validate_token(self, value):
        # Check if the token exists in the EmailVerification model
        email_verification = EmailVerification.objects.filter(token=value).first()

        if not email_verification:
            raise serializers.ValidationError('Invalid token')

        if email_verification.is_expired():
            raise serializers.ValidationError('Token has expired')

        if email_verification.is_verified:
            raise serializers.ValidationError('Email is already verified')

        return value




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Custom token serializer to include both refresh and access tokens in the response.
    """

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        # Customize the response data as needed
        data['refresh_token'] = str(refresh)
        data['access_token'] = data['access']

        return data


class PasswordResetTokenSerializer(serializers.ModelSerializer):
    token = serializers.UUIDField(read_only=True)

    class Meta:
        model = PasswordResetToken
        fields = ['user', 'token', 'created_at']

class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=8, write_only=True)