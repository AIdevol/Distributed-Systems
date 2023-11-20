from django.core.mail import send_mail
from .models import UserProfile


def jwt_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
    }

def send_otp_email(user, otp):
    subject = 'Your OTP Code'
    message = f'Your OTP code is: {otp}'
    from_email = 'devesht709@gmail.com' 
    recipient_list = [user.email]

    send_mail(subject, message, from_email, recipient_list)


def verify_otp(user, otp):
    user_profile = UserProfile.objects.get(user=user)
    if user_profile.otp == otp:
        #if otp is valid
        user_profile.otp = None
        user_profile.save()
        return True
    else:
        # OTP is invalid
        return False

