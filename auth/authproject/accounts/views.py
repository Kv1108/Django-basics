from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.authtoken.models import Token
import random
from django.core.mail import send_mail
from .models import EmailOTP

class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)
    
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message":"Login Successful"})
        
        return Response(serializer.errors, status=400)

class LoginTokenAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            token,_=Token.objects.get_or_create(user=user)

            return Response({"token":token.key})
        
        return Response(serializer.errors, status=400)
    
class SendOTPAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = str(random.randint(100000, 999999))

        EmailOTP.objects.create(email=email, otp=otp)

        send_mail(
            'Your OTP',
            f'Your OTP is {otp}',
            'noreply@test.com',
            [email]
        )

        return Response({"message": "OTP sent"})
    
class VerifyOTPAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if EmailOTP.objects.filter(email=email, otp=otp).exists():
            return Response({"message":"OTP verified"})
        
        return Response({"error":"Invalid OTP"}, status=400)