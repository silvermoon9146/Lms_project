from django.contrib.auth import login, logout
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils import timezone
from datetime import timedelta
from .tasks import *

from .permissions import *
from .serializers import *


class RegisterApiView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
        return user


class CustomLoginApiView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated & IsOwner]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({"detail": "کاربر با موفقیت خارج شد"}, status=200)
        except Exception:
            return Response({"detail": "توکن اشتباه بود"}, status=400)

class RequestPasswordResetView(generics.GenericAPIView):
    serializer_class = RequestPasswordResetSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data['phone']

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return Response({'detail':'کاربری با این شماره یافت نشد'}, status=404)

        otp_instance, created = PasswordResetOTP.objects.get_or_create(phone=phone, is_used=False)
        otp_code = otp_instance.generate_otp()

        send_otp_sms_task.delay(phone, otp_code)
        return Response({'detail': 'کد تایید ارسال شد'}, status=200)

class VerifyOTPAndResetPasswordView(generics.GenericAPIView):
    serializer_class = VerifyOTPAndResetPasswordSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data['phone']
        otp_code = serializer.validated_data['otp_code']
        new_password = serializer.validated_data['new_password']

        try:
            otp_instance = PasswordResetOTP.objects.filter(
                phone=phone,
                otp_code=otp_code,
                is_used=False,
                created_at__gte=timezone.now() - timedelta(minutes=2)
            ).latest('created_at')

        except PasswordResetOTP.DoesNotExist:
            return Response({'detail':'کد تایید منقضی شده است'}, status=400)

        user = User.objects.get(phone=phone)
        user.set_password(new_password)
        user.save()
        otp_instance.is_used = True
        otp_instance.save()

        return Response({'detail':'رمز عبور با موفقیت تغییر کرد'}, status=200)