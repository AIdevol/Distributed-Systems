from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import CustomUserSerializer, CustomUserLoginSerializer  
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate  

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserLogin(APIView):
    def post(self, request):
        serializer = CustomUserLoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            user = None

            if username:
                user = authenticate(username=username, password=password)
            elif email:
                user = authenticate(email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                access_token = refresh.access_token

                return Response({
                    'access': str(access_token),
                    'refresh': str(refresh),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
##############################################################################################################
from rest_framework.permissions import IsAuthenticated
from .authentication import CustomAuthentication

class ProtectedView(APIView):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self):
        user_data = {
            'username': CustomUser.username,
            'email': CustomUser.email,
            'first_name': CustomUser.first_name,
            'last_name': CustomUser.last_name,
            'gender':CustomUser.gender,
            'phone_number':CustomUser.phone_number,
            
        }
        return Response({'message': 'You are authenticated!', 'user_data': user_data})

##############################################################################################################


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user