from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, EmailVerificationSerializer  , CustomTokenObtainPairSerializer , PasswordResetTokenSerializer ,  PasswordResetSerializer
from .models import EmailVerification , PasswordResetToken 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode




class SignInView(TokenObtainPairView):
    """
    Custom SignInView that extends TokenObtainPairView.
    This view returns a JWT token upon successful authentication.
    """
    permission_classes = [AllowAny] 
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == status.HTTP_200_OK:
            # If authentication is successful, add the refresh and access tokens to the response
            refresh_token = response.data.get('refresh_token')
            access_token = response.data.get('access_token')

            # Customize the response data as needed
            data = {
                'refresh_token': refresh_token,
                'access_token': access_token,
            }

            return Response(data, status=status.HTTP_200_OK)

        return response
    

class SignUpView(APIView):
    """
    Custom SignUpView that allows users to register.
    Sends a verification email and returns a JWT token upon successful registration.
    """
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Create an email verification entry
            email_verification = EmailVerification.objects.create(user=user)
            email_verification.send_verification_email()

            # You can customize the response data as needed
            return Response({'message': 'Verification email sent'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmailAPIView(APIView):
    """
    Custom VerifyEmailAPIView to handle email verification.
    """
    permission_classes = [AllowAny] 
    def get(self, request, *args, **kwargs):
        token = self.request.query_params.get('token')

        if not token:
            return Response({'message': 'Token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        email_verification = get_object_or_404(EmailVerification, token=token)

        if email_verification.is_expired():
            return Response({'message': 'Token has expired'}, status=status.HTTP_400_BAD_REQUEST)

        if email_verification.is_verified:
            return Response({'message': 'Email is already verified'}, status=status.HTTP_400_BAD_REQUEST)

        # Mark the email as verified
        email_verification.user.email_verified = True
        email_verification.user.save()

        # success message
        return Response({'message': 'Email verified successfully'}, status=status.HTTP_200_OK)
    





class ForgotPasswordView(generics.CreateAPIView):
    permission_classes = [AllowAny] 
    queryset = PasswordResetToken.objects.all()
    serializer_class = PasswordResetTokenSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user:
                # Check if there is an existing token for the user
                existing_token = PasswordResetToken.objects.filter(user=user).first()
                if existing_token:
                    # Delete the existing token
                    existing_token.delete()

                # Generate a unique token for the user
                new_token = PasswordResetToken.objects.create(user=user)
                # Send the reset link to the user's email
                new_token.send_verification_email()

                return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)



class PasswordResetView(generics.UpdateAPIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        password = request.data.get('password')

        if not token or not password:
            return Response({'message': 'Token and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Find the user associated with the token
        reset_token = PasswordResetToken.objects.filter(token=token).first()
        user = reset_token.user if reset_token else None

        if user:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            # Set the new password for the user
            user.set_password(serializer.validated_data['password'])
            user.save()

            # Delete the used password reset token
            reset_token.delete()

            return Response({'message': 'Password reset successfully'}, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)