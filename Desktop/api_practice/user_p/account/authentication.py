from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        user =request.user
        if user is None or not user.is_authenticated:
            raise AuthenticationFailed('Authentication credentials were not provided.')
        return (user, None)
