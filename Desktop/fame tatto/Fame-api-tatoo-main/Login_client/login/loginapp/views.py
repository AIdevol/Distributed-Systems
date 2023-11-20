import string
import random
from django.core.mail import send_mail  # Import send_mail function
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import UserProfile
from django.conf import settings

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            otp = ''.join(random.choice(string.digits) for _ in range(6))

            user_profile, created = UserProfile.objects.get_or_create(user=user)
            user_profile.otp = otp
            user_profile.save()

            # Send the OTP via email
            send_otp_email(user.email, otp)  # Pass user's email to send_otp_email

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'access_token': access_token,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response(
                {
                    'user_id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'access_token': access_token,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

def send_otp_email(email, otp):
    try:
        subject = "Password Reset OTP"
        message = f'Your OTP for password reset is: {otp}'  
        sender = settings.EMAIL_HOST_USER 
        recipient = [email]

        # Use send_mail function to send the email
        send_mail(
            subject,
            message,
            sender,
            recipient,
            fail_silently=False,
        )
    except Exception as e:
        return str(e)
