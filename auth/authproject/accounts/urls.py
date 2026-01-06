from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LoginTokenAPIView, SendOTPAPIView, VerifyOTPAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('token-login/', LoginTokenAPIView.as_view()),
    path('send-otp/', SendOTPAPIView.as_view()),
    path('verify-otp/', VerifyOTPAPIView.as_view()),

]