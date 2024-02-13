from django.urls import path
from . import views

urlpatterns = [
    # other URL patterns
    path('login/', views.SignInView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('verify-email/', views.VerifyEmailAPIView.as_view(), name='verify_email'),

    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', views.PasswordResetView.as_view(), name='reset-password'),
]