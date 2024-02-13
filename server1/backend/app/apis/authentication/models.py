
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
import uuid


class EmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)


    def is_expired(self):
        expiration_time = self.created_at + timezone.timedelta(days=settings.EMAIL_VERIFICATION_EXPIRATION_DAYS)
        return timezone.now() > expiration_time

    def send_verification_email(self):
        subject = 'Verify your email'
        message = f'Click the following link to verify your email: {settings.FRONTEND_URL}/verify-email/?token={str(self.token)}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.user.email]

        send_mail(subject, message, from_email, recipient_list)



class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Token for {self.user.username}"
    
    def send_verification_email(self):
        subject = 'Password Reset'
        message = f'Click the following link to reset your password: {settings.FRONTEND_URL}/reset-password/?token={str(self.token)}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [self.user.email]
        send_mail(subject, message, from_email, recipient_list)

